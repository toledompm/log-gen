import time
import random

# {"env":"XXX","path":"XXX","method":"XXX","duration":XXX,"statusCode":XXX,"statusMessage":"XXX","host":"XXX","level":"XXX","message":"XXX","timestamp":"XXX"}​
env = ["prod"]
paths = ["/", "/path1", "/path2", "/api/path3"]
methods = ["GET", "POST", "PUT", "DELETE"]
status_code = [200, 300] + list(range(400, 600))
status_message = ["status message 1", "status message 2", "status message 3"]
host = ["queroteste.com"]
level = ["LEVEL 1", "LEVEL 2", "LEVEL 3"]
message = ["message 1", "message 2", "message 3"]

def generate_log():
    return {
        "env": str(random.choice(env)),
        "path": str(random.choice(paths)),
        "method": str(random.choice(methods)),
        "duration": str(random.choice(range(0, 1000))),
        "statusCode": str(random.choice(status_code)),
        "statusMessage": str(random.choice(status_message)),
        "host": str(random.choice(host)),
        "level": str(random.choice(level)),
        "message": str(random.choice(message)),
        "timestamp": str(time.time())
    }


def log_to_file(logfile, log):
    with open(logfile, "a") as f:
        f.write(str(log) + "\n")
        f.close()

def clear_log_file(logfile):
    with open(logfile, "w") as f:
        f.write("")
        f.close()


def main():
  log_file = "/tmp/log.txt"
  count = 0
  while True:
      time.sleep(0.5)
      log_to_file(log_file, generate_log())
      count += 1
      if count == 1000:
          clear_log_file(log_file)
          count = 0

main()
