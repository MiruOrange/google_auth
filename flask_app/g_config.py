bind = "0.0.0.0:8000"
workers =5
loglevel = 'debug'
access_log_format = "{'request_date':%(t)s, 'remote_ip':%(h)s,'request_id':%({X-Request-Id}i)s,'response_code':%(s)s,'request_method':%(m)s,'request_path':%(U)s,'request_querystring': %(q)s>"
timeout = 1220
accesslog = "/var/log/gunicorn/access.log"  
errorlog = "/var/log/gunicorn/error.log" 
