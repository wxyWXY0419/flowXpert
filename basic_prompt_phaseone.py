cand = """
## POSSIBLE ROOT CAUSE REASONS:

### Service-Level
- network delay
- network loss
- network corrupt
- cpu stress
- memory stress
- pod failure
- pod kill
- jvm exception
- jvm gc
- jvm latency
- jvm cpu stress
- dns error
- target port misconfig
- code error

### Pod-Level
- cpu stress
- memory stress
- pod failure
- pod kill
- jvm exception
- jvm gc
- jvm latency
- jvm cpu stress
- dns error
- io fault

### Node-Level
- node cpu
- node disk
- node network loss
- node network delay

## POSSIBLE ROOT CAUSE COMPONENTS:

### Nod-Level
- aiops-k8s-01
- aiops-k8s-02
- aiops-k8s-03
- aiops-k8s-04
- aiops-k8s-05
- aiops-k8s-06
- aiops-k8s-07
- aiops-k8s-08

### Service-Level
- adservice
- cartservice
- checkoutservice
- currencyservice
- emailservice
- frontend
- paymentservice
- productcatalogservice
- recommendationservice
- redis-cart
- shippingservice
- tidb-tidb
- tidb-pd
- tidb-tikv

## Pod-Level
- adservice-0
- adservice-1
- adservice-2
- cartservice-0
- cartservice-1
- cartservice-2
- checkoutservice-0
- checkoutservice-1
- checkoutservice-2
- currencyservice-0
- currencyservice-1
- currencyservice-2
- emailservice-0
- emailservice-1
- emailservice-2
- frontend-0
- frontend-1
- frontend-2
- paymentservice-0
- paymentservice-1
- paymentservice-2
- productcatalogservice-0
- productcatalogservice-0
- productcatalogservice-1
- productcatalogservice-2
- recommendationservice-0
- recommendationservice-1
- recommendationservice-2
- shippingservice-0
- shippingservice-1
-shippingservice-2
- redis-cart-0
"""

schema = """## PHASEONE DATASET DIRECTORY STRUCTURE:

- You can access the phaseone dataset directory in our microservice system:`dataset/phaseone/`.
 
- This directory contains subdirectories organized by a date(e.g.,`dataset/phaseone/2025-06-06/`).

- Within each date-specific directory, you'll find these subdirectories:`log-parquet`,`metric-parquet`,`trace-parquet`(e.g.,`dataset/phaseone/2025-06-06/log-parquet/`).

- All telemetry data is stored in the Parquet format (`.parquet`), with the date and hour typically included in the filename (e.g., `dataset/phaseone/2025-06-06/log-parquet/log_filebeat-server_2025-06-06_00-00-00.parquet`).

- Within each `metric-parquet` directory, you'll find these subdirectories:`apm`,`infra`,`other`().

- The `metric-parquet` directory is further organized by the source of the metrics:

  - `apm`: Contains metrics that collected in the cluster by the DeepFlow system, subdivided by business namespace such as `pod` and `service` (e.g., `dataset/phaseone/2025-06-06/metric-parquet/apm/pod/pod_adservice-0_2025-06-06.parquet`).

  - `infra`: Holds infrastructure metrics, subdivided into `infra_node`(node-level), `infra_pod`(pod-level), and `infra_tidb`(related to TiDB components) (e.g., `dataset/phaseone/2025-06-06/metric-parquet/infra/infra_node/infra_node_node_cpu_usage_rate_2025-06-06.parquet`).

  - `other`: Includes metrics from other specialized components like `pd` and `tikv` (e.g., `dataset/phaseone/2025-06-06/metric-parquet/other/infra_pd_abnormal_region_count_2025-06-06.parquet`).

## DATA SCHEMA

1. **Metric Files**:

    1.`apm/**/*.parquet`:

        ```parquet
        time,client_error,client_error_ratio,error,error_ratio,object_id,object_type,request,response,rrt,rrt_max,server_error,server_error_ratio,timeout
        2025-05-05 16:04:00+00:00,0,0.00,0,0.00,adservice-0,pod,325,328,3661.83,43319,0,0,0
        ```
    
    2.`infra/**/*.parquet`:

        ```parquet
        time,cf,device,instance,kpi_key,kpi_name,kubernetes_node,mountpoint,namespace,object_type,pod,value,sql_type,type
        The `kpi_key` column defines the type of the metric, and the `value` column is its corresponding value.

        2025-05-05 16:04:00+00:00,null,null,aiops-k8s-01,pod_cpu_usage,CPU使用率,null,null,hipstershop,pod,emailservice-2,0.0,null,null
        ```

2. **Trace Files**

    1.`trace_jaeger-span_2025-06-*_*-00-00.parquet`
    traceID,spanID,flags,operationName,references,startTime,startTimeMillis,duration,tags,logs,process
    063346d9fb108c5fd56ecdeb9aae4e97,a5dbaca343f5bf6b,1.0,hipstershop.CurrencyService/GetSupportedCurrencies,[{'refType': 'CHILD_OF', 'spanID': '0473d09282f6f37b'}],1746028800342964,1746028800342,4202,[{'key': 'rpc.system', 'type': 'string', 'value': 'grpc'}, {'key': 'span.kind', 'type': 'string', 'value': 'server'}, {'key': 'rpc.grpc.status_code', 'type': 'int64', 'value': 0}],[{'fields': [{'key': 'message.type', 'type': 'string', 'value': 'EVENT'}, {'key': 'message.event', 'type': 'string', 'value': 'ServerRecv'}], 'timestamp': 1746028800343000}],{'serviceName': 'frontend', 'tags': [{'key': 'hostname', 'type': 'string', 'value': 'frontend-xyz'}]}

3. **Log Files**

    1.`log_filebeat-server_2025-06-*_*-00-00.parquet`
    k8_namespace,@timestamp,agent_name,k8_pod,message,k8_node_name
    hipstershop,2025-05-27T00:00:00Z,filebeat-filebeat-bdkxq,cartservice-2,Executed endpoint 'gRPC - /hipstershop.C...,aiops-k8s-03

{cand}

## CLARIFICATION OF TELEMETRY DATA:

1. Please note the following file naming conventions:

    1. In the path `/phaseone/**/metric-parquet/apm/pod/`,the filenames contain the pod names(e.g.,`pod_adservice-0_2025-06-06.parquet`, the pod name is adservice-0).

    2. In the path `/phaseone/**/metric-parquet/apm/service`, the filenames contain the service names(e.g.,`service_adservice_2025-06-06.parquet`, the service name is adservice).

    3. In the path `/phaseone/**/metric-parquet/infra/**/`, the filenames contain the kpi_key(e.g.,`infra_node_node_cpu_usage_rate_2025-06-06.parquet`, the kpi_key is node_cpu_usage_rate).

2. The files in the path `/phaseone/**/metric-parquet/apm/**/` contains 9 KPIs :client_error,client_error_ratio,error,error_ratio,rrt,rrt_max,server_error, server_error_ratio and timeout. In contrast, files in the path `/phaseone/**/metric-parquet/infra/**/` records a variety of KPIs, such as node cpu usage. The specific names of these KPIs can be found in the `kpi_key` and `kpi_name` fields.

3. In different data files, the timestamp units and timezones may vary:

- **Filenames**: Timestamps are strings representing China Standard Time(CST, UTC+8)(e.g.,2025-06-06).

- **Log**: The timestamp is provided in the `@timestamp` field as a UTC ISO 8601 strings with millisecond precision(e.g., 2025-06-05T16:00:29.045Z).

- **Metric**: The timestamp is provided in the `time` field as a UTC ISO 8601 strings(e.g.,2025-06-05T16:00:00Z).

- **Trace**: The timestamp is provided in the `startTimeMillis` field as a Unix timestamp in milliseconds (e.g., 1749139200377).

4. Please use the UTC+8 time zone in all analysis steps since system is deployed in China.
"""