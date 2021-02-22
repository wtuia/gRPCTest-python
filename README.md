1.安装gRPC:python -m pip install grpcio

2.安装gRPC工具:python -m pip install grpcio-tools

3.运行命令:>python -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos/helloworld.proto
其中:protos 为配置文件父目录路径,protos/helloworld.proto为配置文件

4.编写客户端/服务端

    