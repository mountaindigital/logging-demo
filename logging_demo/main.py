import datetime
import logging
import time

import google.cloud.logging as gcp_logging

def main():
    client = gcp_logging.Client()
    client.setup_logging()
    
    while True:
        now = datetime.datetime.now()
        logging.info(f'VM is running at {now}')
        time.sleep(60)

if __name__ == '__main__':
    main()