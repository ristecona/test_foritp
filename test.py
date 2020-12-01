# Hello World program in Python
contacts_list=[['Alice Brown','','1231112223'],['Bob Crown','bob@crowns.com',''],['Carlos Drew','carl@drewess.com','3453334445'],\
	['Doug Emerty','','4564445556'],['Egan Fair','eg@fairness.com','5675556667']]
	
leads_list=[['','kevin@keith.com',''],['Lucy','lucy@liu.com','3210001112'],['Mary Middle','mary@middle.com','3331112223'],\
	['','','4442223334'],['','ole@olson.com','']]
	
	
json={'registrant': [{'name': 'Lucy Liu', 'email': 'lucy@liu.com', 'phone': ''},\
    {'name': 'Doug', 'email': 'doug@emmy.com', 'phone': '4564445556'},\
    {'name': 'Uma Thurman','email':'uma@thurs.com','phone':''}]
}
for i in json['registrant']:
    matched=False
    for sublist in contacts_list:
        if i['email'] and i['email']==sublist[1]:
            if not sublist[0] and i['name']!='':
                sublist[0]=i['name']
            if not sublist[2] and i['phone']!='':
                sublist[2]=i['phone']
            matched=True
        if i['phone'] and i['phone']==sublist[2] and not matched:
            if not sublist[0] and i['name']!='':
                sublist[0]=i['name']
            if not sublist[1] and i['email']!='':
                sublist[1]=i['email']
            matched=True
    
    if not matched:
        for sublist in leads_list:
            if i['email'] and i['email']==sublist[1]:
                if not sublist[0] and i['name']!='':
                    sublist[0]=i['name']
                if not sublist[2] and i['phone']!='':
                    sublist[2]=i['phone']
                contacts_list.append(sublist)
                leads_list.remove(sublist)
                matched=True
            if i['phone'] and i['phone']==sublist[2] and not matched:
                if not sublist[0] and i['name']!='':
                    sublist[0]=i['name']
                if not sublist[1] and i['email']!='':
                    sublist[1]=i['email']
                contacts_list.append(sublist)
                leads_list.remove(sublist)
                matched=True
    #ITS NOWHERE
    if not matched:
        new_contact=list(i.values())
        contacts_list.append(list(i.values()))
print(contacts_list)
print(leads_list)