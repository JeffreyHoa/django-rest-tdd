#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    # nc命令用于设置路由器
    # -z 扫描通信端口
    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# 清空数据库
python manage.py flush --no-input

# 将生成的py文件应用到数据库
python manage.py migrate

# 下一步，进入 docker shell.
exec "$@"
