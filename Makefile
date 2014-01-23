attendees.txt: open_government_meeting.html
	./attendees.py > attendees.txt

open_government_meeting.html:
	wget -O open_government_meeting.html https://public.resource.org/open_government_meeting.html
