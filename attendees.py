#!/usr/bin/env python3
import lxml.html

def main():
    html = lxml.html.parse('open_government_meeting.html')
    trs = html.xpath('//table[@width="100%"]/tbody/tr[position()>1]')
    for to in map(email_address, trs):
        print(to + ',')

def email_address(tr):
    name = str(tr.xpath('td[position()=2]')[0].text_content())
    addr = str(tr.xpath('td[position()=3]')[0].text_content())\
        .replace(' [at] ','@').replace(' [dot] ','.')
    return '%s <%s>' % (name, addr)

if __name__ == '__main__':
    main()
