# Delfos Forwarder
# =========================================
#
# TLS encryption to cloud collectors

####
## System
####
<system>
  process_name delfos
  workers 1
  root_dir /opt/buffer
</system>

####
# Sources
####

<source>
  @type udp
    tag device.firewall
    port 40001
    bind 0.0.0.0
    format none
</source>

<source>
  @type beats
    tag device.ad
    port 40002
    bind 0.0.0.0
    format none
</source>

####
# Destinations
####

<match device.*>
  @type forward
  compress gzip
  transport tls
  tls_insecure_mode true
  tls_verify_hostname false
  tls_allow_self_signed_cert true

  <server>
    name colector
    host {{ collector.host }}
    port {{ collector.port }}
  </server>

  <buffer>
      @type file
      @id {{ customer }}
      path /opt/buffer

      chunk_limit_size 5m
      flush_mode interval
      flush_interval 2s
      flush_thread_count 4

      retry_wait 10
      retry_type periodic
      retry_forever true
      disable_chunk_backup true
      total_limit_size 256GB
  </buffer>

</match>