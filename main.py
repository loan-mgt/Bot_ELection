from getNews import getNews
from Tweet import tweet_tread
import pause
from datetime import datetime, date, timedelta
from rich import print




if int(datetime.now().strftime('%H')) < 8:
	d = datetime.now()
	d = datetime(int("20"+d.strftime('%y')),int(d.strftime('%m')),int(d.strftime('%d')),8,0)
	p
    
else:
	d = datetime.now()
	d = datetime(int("20"+d.strftime('%y')),int(d.strftime('%m')),int(d.strftime('%d')),8,0) + timedelta(days=1)
	

print(f"[bold green][INFO][/bold green] tweeting start at {d}")
pause.until(d)

r = getNews()

tweet_tread(r)

while True:
	pause.days(1)
	r = getNews()
	tweet_tread(r)
	print(f"[bold green][INFO][/bold green] tweeted at {datetime.now()} ")


