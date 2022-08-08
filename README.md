# train-ticket-auto-query

Train Ticket Auto Query Python Scripts

## How to use

The scripts have contained some origin scenarios:
* "admin_operations"
* "normal_flow"
* "rebook_flow"
* "rebook_fail_flow"
* "search_fail_add"
* "consign_preserve"

具体使用方法为运行scenarioApi.py脚本并传入以下参数:(type表示参数类型，定义如下)

    # type
    # 0 表示没有peak和valley读入参数为 scenario type init_qps endtimeYMD endtimeHMS
    # 1 表示有peak没有valley读入参数为 scenario type init_qps endtimeYMD endtimeHMS peak_start_time peak_end_time peak_qps
    # 2 表示没有peak有valley读入参数为 scenario type init_qps endtimeYMD endtimeHMS valley_start_time valley_end_time valley_qps
    # 3 表示peak和valley均有 读入参数为 scenario type init_qps endtimeYMD endtimeHMS peak_start_time peak_end_time peak_qps valley_start_time valley_end_time valley_qps
    # 其中endtime为%Y-%m-%d %H:%M:%S格式 分成endtimeYMD和endtimeHMS两个参数
    # 各种end\start time为 %H:%M:%S格式
    
### tips:
* 所部署ts服务的地址在constant.py中修改
* 脚本默认线程池大小为100，可以进行修改，在scenarioApi.py中修改参数
* 服务仍存在部分bug使脚本流程无法完美运行
