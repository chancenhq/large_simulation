import multiprocessing

# Gunicorn configuration for Render deployment
bind = "0.0.0.0:10000"  # Render uses port 10000 by default
workers = multiprocessing.cpu_count() * 2 + 1
threads = 2
worker_class = "gthread"
timeout = 120
keepalive = 5
max_requests = 1000
max_requests_jitter = 50
preload_app = True
accesslog = "-"  # Log to stdout
errorlog = "-"   # Log to stderr
loglevel = "info" 