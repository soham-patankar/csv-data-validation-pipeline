import csv

try:
    with open('customers_2000.csv','r') as f:
         reader=csv.reader(f)
         exp1=['customer_id','name','phone','email','city']
         head1=next(reader)
         val1=[]
         inval1=[]  
         ids=set()
         if head1!=exp1:
             print('Wrong header!')
             exit()
         else:
             for r in reader:
                 if len(r)!=5:
                    print('Broken row')
                    inval1.append(r)
                    continue
                 else:
                    cid=r[0]
                    name=r[1]
                    num=r[2]
                    email=r[3]
                    city=r[4]

                    if not cid.isdigit() or cid in ids:
                       inval1.append(r)
                       continue
                    if name.strip()=='' or city.strip()=='':
                       inval1.append(r)
                       continue
                    if not num.isdigit() or len(num)!=10:
                       inval1.append(r)
                       continue
                    if not '@' in email:
                       inval1.append(r)
                       continue   
                    ids.add(cid)
                    val1.append(r) 
    with open('val1rec.csv','w') as k:
         writer=csv.writer(k)
         writer.writerow(head1)
         writer.writerows(val1) 
    with open('inval1rec.csv','w') as k:
         writer=csv.writer(k)
         writer.writerow(head1)
         writer.writerows(inval1)          
    with open('orders_5000.csv','r') as p:
         reader=csv.reader(p)
         head2=next(reader)
         exp2=['order_id','customer_id','product','quantity','amount']            
         val2=[]
         inval2=[]  
         ods=set() 
         if head2!=exp2:
             print('Wrong Header')
             exit()
         else:
             for r in reader:
                 if len(r)!=5:
                     print('Broken Row!')
                     inval2.append(r)
                     continue
                 else:
                     oid=r[0]
                     cid=r[1]
                     prod=r[2]
                     qnty=r[3]
                     amt=r[4]

                     if not oid.isdigit() or oid in ods:
                         inval2.append(r)
                         continue
                     if prod.strip()=='':
                         inval2.append(r)
                         continue
                     if not qnty.isdigit() or int(qnty)<=0:
                         inval2.append(r)
                         continue
                     if not amt.isdigit() or int(amt)<=0:
                         inval2.append(r)
                         continue
                     if not cid in ids:
                         inval2.append(r)
                         continue
                     ods.add(oid)
                     val2.append(r)  
    with open('val2rec.csv','w') as k:
         writer=csv.writer(k)
         writer.writerow(head2)
         writer.writerows(val2) 
    with open('inval2rec.csv','w') as k:
         writer=csv.writer(k)
         writer.writerow(head2)
         writer.writerows(inval2)                    
except Exception as e:
    print('A problem occurred',e)
