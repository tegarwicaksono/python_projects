import time
from datetime import datetime as dt


hosts_temp   = "hosts"
hosts_path   = "C:\Windows\System32\drivers\etc\hosts"
redirect     = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]


def blocking_time():
	blocking_time_start = 8	# starting at 8AM
	blocking_time_end   = 17 # ending at 5PM
	return dt(dt.now().year,dt.now().month,dt.now().day, 8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,19)


while True:
	if blocking_time():
		print("Working hours")
		with open(hosts_path, "r+") as input_file:
			content = input_file.read()
			for website in website_list:
				if website in content:
					pass
				else:
					input_file.write(redirect + " " + website + "\n")
	else:
		with open(hosts_path,"r+") as input_file:
			content = input_file.readlines()
			input_file.seek(0)
			for line in content:
				if not any(website in line for website in website_list):
					input_file.write(line)
			input_file.truncate()

		print("Happy hours")

	time.sleep(5)

