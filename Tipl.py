import subprocess as sp
import pymysql
import pymysql.cursors
import re
elist = []

elist = [
    [["Tid", "int"], ["Team","str"],["Thome","str"], ["W","int"], ["L","int"],["D","int"], ["captainpassport_no","str"], ["captaincountry","str"], ["Tname", "str"]],

    [ ["passport_number","str"], ["Pcountry","str"] , ["Player_first_name","str"] , ["player_middle_name","str"],
     ["player_last_name","str"] , ["Matches_played","int"] , ["DOB","str"] , ["Playing_team_id","int"] ],

    [["Stage","str"], ["Venue","str"] , ["TeamA_id","int"] , ["TeamB_id","int"] , ["TeamA_score","int"] , ["TeamB_score","int"] , ["Matchnumber","int"] ],

    [["Capacity","int"], ["name","str"] , ["Vcity","str"]] ,

    [["IPLSTAGE","str"] , ["From_date","str"] , ["To_date","str"]],

    [["passport_number", "str"] , ["player_country" , "str"] , ["Number_of_runs" , "int"], ["Average_runs", "int"]],

    [["passport_number", "str"] , ["player_country" , "str"] , ["Number_of_wickets" , "int"]],

    [["CoachTid", "int"] , [ "coachname" , "str"] , ["Supercoachname" ,"str"]],

    [["Sponsor_percentage" , "int"] , ["Sponsor_name" , "str"]],

    [ ["Sponsor", "str"],["Team_id", "int"] ],

    [["Dppassport_number" , "str"] , ["Dpcountry" , "str"] , ["Name","str"] ,["Relation" , "str"] , ["Age","str"]],

    [["Player_passport_Number" , "str"] , [ "Player_country", "str"] , ["Location", "str"]]    

]

stage = [ "League" , "Playoffs", "Final" ]

elists = [
    [ ["Team","str"],["Thome","str"], ["captainpassport_no","str"], ["captaincountry","str"] , ["Tname", "str"]] ,
    [ ["player_first_name","str"] , ["player_middle_name","str"],
     ["player_last_name","str"]  , ["DOB","str"] , ["playing_team_id","int"] ],

    [ ["Stage","str"], ["Venue","str"] , ["TeamA_id","int"] , ["TeamB_id","int"] , ["TeamA_score","int"] , ["TeamB_score","int"] , ["Matchnumber","int"] ],

    [ ["Capacity","int"] ] ,

    [ ["IPLSTAGE","str"] , ["From_date","str"] , ["To_date","str"] ],

    [ ["Number_of_runs" , "int"], ["Average_runs", "float"] ],

    [ ["Number_of_wickets" , "int"] ],

    [ ["Supercoachname" ,"str"]],

    [ ["Sponsor_percentage" , "int"]  ],

    [ ["Sponsor", "str"],["Team_id", "int"] ],

    [ ["Name","str"] ,["Relation" , "str"] , ["Age","str"]],

    [ ["Location", "str"]]

]

general  = [1,2,3,4,5,6,7,8,9,10,11,12]

def analysis():
    print("1. Leading scorer from a Team")
    print("2. Leading wicket taker from a Team")
    print("3. To know the venue is batting pitch or bowling pitch")
    try:
        ch = int(input("Enter choice> "))
      #  tmp = sp.call('clear', shell=True)
       
    except:
        print("Sorry the input is not a number!")
        return -1
    try:
        if ch==1 or ch==2:
            print("Give atleast one of the details to find a team")
            cou=0
            couc = len(elist[0])
            cou = 0        
            val = {}
            for i in elist[0]:
                if (i[1] == "str"):
                    sto=input(i[0]+ " : ")
                    if len(sto) == 0:
                        continue
                    else:
                        sto = "'"+str(sto)+"'"
                        val[i[0]]=sto 
                elif i[1] == "int":
                    sto=input(i[0]+ " : ")
                    if len(sto)==0:
                        continue
                    else:
                        sto= float(sto)
                        sto = int(sto)
                        val[i[0]]=sto
            strings = ""
            couc=len(val)
            if couc == 0:
                print("Nothing was selected please try again :(")
                return 0
            cou = 0
            for i,j in val.items():
                cou = cou + 1
                if cou <  couc:
                    strings = strings + str(i)+ "=" + str(j) + " AND "
                elif cou==couc:
                    strings = strings + str(i) + "= "+ str(j)+"  "
            cur.execute("SELECT Tid FROM TEAM WHERE "+ strings)
            x=cur.fetchall()
            if len(x)==0:
                print("No results found please try again later")
                return 0
            for k in x:
                for kkk,ii in k.items():
                    if ch==1:
                        cur.execute("SELECT * FROM  (SELECT PLAYER.Player_first_name,PLAYER.player_last_name,BATSMAN.Number_of_runs FROM PLAYER JOIN BATSMAN ON PLAYER.passport_number=BATSMAN.passport_number AND PLAYER.Pcountry=BATSMAN.player_country  AND  PLAYER.Playing_team_id = "+str(ii)+" ) AS totals ORDER BY totals.Number_of_runs DESC")
                        a11=cur.fetchone()
                        print("The highest score is "+str(a11['Number_of_runs'])+" scored by "+ a11['Player_first_name']+" "+a11['player_last_name'])
                    elif ch==2:
                        cur.execute("SELECT * FROM  (SELECT PLAYER.Player_first_name,PLAYER.player_last_name,BOWLER.Number_of_wickets FROM PLAYER JOIN BOWLER ON PLAYER.passport_number=BOWLER.passport_number AND PLAYER.Pcountry=BOWLER.player_country  AND  PLAYER.Playing_team_id = "+str(ii)+" ) AS totals ORDER BY totals.Number_of_wickets DESC")
                        a11=cur.fetchone()
                        print("The highest number of wickets are "+str(a11['Number_of_wickets'])+" scored by "+ a11['Player_first_name']+" "+a11['player_last_name'])
        elif ch==3:
            print("Give atleast one of the details for venue")
            cou=0
            couc = len(elist[3])
            cou = 0        
            val = {}
            for i in elist[3]:
                if (i[1] == "str"):
                    sto=input(i[0]+ " : ")
                    if len(sto) == 0:
                        continue
                    else:
                        sto = "'"+str(sto)+"'"
                        val[i[0]]=sto 
                elif i[1] == "int":
                    sto=input(i[0]+ " : ")
                    if len(sto)==0:
                        continue
                    else:
                        sto = float(sto)
                        sto = int(sto)
                        val[i[0]]=sto
            strings = ""
            couc=len(val)
            if couc == 0 :
                print("Nothing is provided please try again :(")
                return 0
            cou = 0
            for i,j in val.items():
                cou = cou + 1
                if cou <  couc:
                    strings = strings + str(i)+ "=" + str(j) + " AND "
                elif cou==couc:
                    strings = strings + str(i) + "= "+ str(j)+"  "
            cur.execute("SELECT name FROM VENUE WHERE "+ strings)
            x=cur.fetchall()
            if len(x)==0:
                print("No results found please try again later")
                return 0
            for k in x:
                for kkk,ii in k.items():
                    cur.execute("SELECT COUNT(*) AS COUNT,SUM(TeamA_score) AS SUM_A,SUM(TeamB_score) AS SUM_B FROM MATCHES WHERE VENUE ="+ "'" + str(ii)+"'")
                    a11=cur.fetchone()
                    if len(a11)==0:
                        print("No results found please try again later")
                        return 0
                    tot=(int(a11['SUM_A'])+int(a11['SUM_B']))/float(a11['COUNT'])
                    if tot<300:
                        print(ii+" is a Bowling pitch")
                    else:
                        print(ii+" is a Batting pitch") 


    except Exception as e:
        con.rollback()
        print("Failed to analyse of database")
        print(">>>>>>>>>>>>>", e)


def aggregation():
    print("1. Average runs scored by a Team")
    print("2. Average runs scored by a Player")
    # print("3. Maximum score in all Matches")
    # print("4. Maximum runs scored by player")
    # print("5. Maximum wickets by a player")
    try:
        ch = int(input("Enter choice> "))
      #  tmp = sp.call('clear', shell=True)
       
    except:
        print("Sorry the input is not a number!")
        return -1
    try:
        if ch==1:
            print("Give atleast one of the details to find a team")
            cou=0
            couc = len(elist[ch-1])
            cou = 0        
            val = {}
            for i in elist[ch-1]:
                if (i[1] == "str"):
                    sto=input(i[0]+ " : ")
                    if len(sto) == 0:
                        continue
                    else:
                        sto = "'"+str(sto)+"'"
                        val[i[0]]=sto 
                elif i[1] == "int":
                    sto=input(i[0]+ " : ")
                    if len(sto)==0:
                        continue
                    else:
                        sto = float(sto)
                        sto = int(sto)
                        val[i[0]]=sto
            strings = ""
            couc=len(val)
            if couc == 0 :
                print("Nothing is selected please try again :(")
                return 0
            cou = 0
            for i,j in val.items():
                cou = cou + 1
                if cou <  couc:
                    strings = strings + str(i)+ "=" + str(j) + " AND "
                elif cou==couc:
                    strings = strings + str(i) + "= "+ str(j)+"  "
            cur.execute("SELECT Tid FROM TEAM WHERE "+ strings)
            x=cur.fetchall()
            if len(x)==0:
                print("No results found please try again later")
                return 0
            for k in x:
                for kkk,ii in k.items():
                    cur.execute("SELECT TeamA_score FROM MATCHES WHERE TeamA_id = "+str(ii) )
                    a11=cur.fetchall()
                    if len(a11)==0:
                        print("No results found please try again later")
                        return 0
                    cur.execute("SELECT TeamB_score FROM MATCHES WHERE TeamB_id = "+str(ii) )
                    a22=cur.fetchall()
                    if len(a22)==0:
                        print("No results found please try again later")
                        return 0
                    cur.execute("SELECT W,L,D FROM TEAM WHERE Tid = "+str(ii) )
                    a3=cur.fetchall()
                    if len(a3)==0:
                        print("No results found please try again later")
                        return 0
                    nom=0
                    
                    for ele in a3:
                        for ll,kk in ele.items():
                            nom=nom+int(kk)
                    
                    avg=0
                    for a1 in a11:
                        for i,j in a1.items():
                            avg = avg + int(j)
                    for a2 in a22:
                        for i,j in a2.items():
                            avg = avg + int(j)
                    avg=(avg)/float(nom)
                    cur.execute("SELECT Tname FROM TEAM WHERE Tid = "+str(ii) )
                    a4=cur.fetchone()
                    if len(a4)==0:
                        print("No results found please try again later")
                        return 0
                    for i,j in a4.items():
                        print("The average runs scored by "+j+" is "+str(avg) )
        if ch==2:
            print("Give atleast one of the details to find batsman")
            cou=0
            couc = len(elist[ch-1])
            cou = 0        
            val = {}
            for i in elist[ch-1]:
                if (i[1] == "str"):
                    sto=input(i[0]+ " : ")
                    if len(sto) == 0:
                        continue
                    else:
                        sto = "'"+str(sto)+"'"
                        val[i[0]]=sto 
                elif i[1] == "int":
                    sto=input(i[0]+ " : ")
                    if len(sto)==0:
                        continue
                    else:
                        sto = float(sto)
                        sto = int(sto)
                        val[i[0]]=sto
            strings = ""
            couc=len(val)
            if couc == 0 :
                print("Nothing is mentioned please try again :(")
                return 0
            cou = 0
            for i,j in val.items():
                cou = cou + 1
                if cou <  couc:
                    strings = strings + str(i)+ "=" + str(j) + " AND "
                elif cou==couc:
                    strings = strings + str(i) + "= "+ str(j)+"  "
            cur.execute("SELECT passport_number,Pcountry FROM PLAYER WHERE "+ strings)
            x=cur.fetchall()
            if len(x)==0:
                print("No results found please try again later")
                return 0
            for k in x:
                #print(k)
                strings=""
                string=""
                edge=len(k.items())
                for kkk,ii in k.items():
                    edge =edge -1
                    strings=strings + kkk + " = '"+ii + "'"
                    if kkk== "Pcountry":
                        string=string + "player_country" + " = '"+ii + "'"
                    else:
                        string=string + kkk + " = '"+ii + "'"
                    if edge !=0:
                        strings=strings + " AND "
                        string=string+" AND "
                
                cur.execute("SELECT Player_first_name,player_last_name FROM PLAYER WHERE "+strings )
                a11=cur.fetchall()
                if len(a11)==0:
                    print("No results found please try again later")
                    return 0
                cur.execute("SELECT Average_runs FROM BATSMAN WHERE " + string )
                a22=cur.fetchall()
                if len(a22)==0:
                    print("No results found please try again later")
                    return 0
                    # cur.execute("SELECT W,L,D FROM TEAM WHERE Tid = "+str(ii) )
                    # a3=cur.fetchall()
                    # nom=0
                    
                    # for ele in a3:
                    #     for ll,kk in ele.items():
                    #         nom=nom+int(kk)
                    
                    # avg=0
                strname=""
                for a1 in a11:
                    for i,j in a1.items():
                        strname=strname + " "+ j
                score=""
                for a2 in a22:
                    for i,j in a2.items():
                        score=score+str(j)
                # avg=(avg)/float(nom)
                # cur.execute("SELECT Tname FROM TEAM WHERE Tid = "+str(ii) )
                # a4=cur.fetchone()
                # for i,j in a4.items():
                print("The average runs scored by "+strname +" is "+score )
        

    except Exception as e:
        con.rollback()
        print("Failed to find aggregate of database")
        print(">>>>>>>>>>>>>", e)

    return


def fsearch(ch,strig,choice):
    try:
        matchword = input("Please enter the word that you want to match: ")
        var = "SELECT * FROM " + strig
        cur.execute(var)
        vari = cur.fetchall()
        for i in vari:
            if len(re.findall(matchword,str(i[elist[ch-1][choice-1][0]])))!=0:
                for j,k in i.items():
                    print(f"{j} : {k}")   
                print("++++++++++++++++++")
                
    except Exception as e:
        con.rollback()
        print("Failed when searching")
        print(">>>>>>>>>>>>>", e)

    return
        
   

def fselect(strig):
    try:
        query = "select * from " + strig
        cur.execute(query)
        vari = cur.fetchall()
        for i in vari:
            for j,k in i.items():
                print(f"{j} : {k}")   
            print("++++++++++++++++++")
    except:
        print("Unexpected behaviour")
        
def finsert(ch,namena):
    try:
        strings = " ( "
        couc=len(elist[ch-1])
        cou = 0
        for i in elist[ch-1]:
            cou = cou + 1
            if cou !=  couc:
                strings = strings + i[0] + " , "
            else:
                strings = strings + i[0] + " ) "
        cou=0
        string2 = " ( "
        for i in elist[ch-1]:
            cou = cou + 1
            if cou !=  couc:
                if i[1] == "str" :
                    string2 = string2 + " %s " + " , "
                elif i[1] == "int":
                    string2 = string2 + " %s "+ " , "
            else:
                if i[1] == "str" :
                    string2 = string2 + " %s " + " ) "
                elif i[1] == "int" :
                    string2 = string2 + " %s "+ " ) "


        cou = 0
        print("Please add the info of the follwing details")
        val = []
        for i in elist[ch-1]:
            if i[0]=="IPLSTAGE" or i[0]=="Stage":
                try:
                    print("choose Among the three options")
                    print("---------1."+stage[0])
                    print("---------2."+stage[1])
                    print("---------3."+stage[2])
                    ct = int(input("enter choice >"))
                    if(ct>3):
                        print("Invalid option :(")
                        return -1
                    if(ct<1):
                        print("Invalid option :(")
                        return -1
                    sto = stage[ct-1]
                except:
                    print("Invalid response recieved :'(")
                    return -1
            elif (i[1] == "str"):
                sto=input(i[0]+ " : ")
                if len(sto)==0:
                    sto=None
                else:
                    sto = str(sto)
            elif i[1] == "int":
                sto=input(i[0]+ " : ")
                if len(sto)==0:
                    sto=None
                else:
                    sto = float(sto)
                    sto = int(sto)
            val.append(sto)
        vall=val
        val = tuple(val)
        finalstring = "insert into " + namena + strings + " VALUES " + string2
        cur.execute(finalstring , val)
        if ch==2:
            sto=input("If the player is a Batsman press enter else press any other key : ")
            if len(sto)==0:
                nof=input("Number of runs scored by so far >> ")
                nof = int(nof)
                if val[5]!=0:
                    avg = nof/val[5]
                else:
                    avg=0
                cur.execute("insert into BATSMAN VALUES (%s , %s , %s ,%s)",(val[0],val[1],int(nof), avg))
            else:
                nof=input("Number of wickets picked so far >> ")
                cur.execute("insert into BOWLER VALUES (%s , %s , %s )",(val[0],val[1],int(nof)))

            while(1):
                address = input("Enter the addresses of the player if u are done press ENTER >> ")
                if len(address) == 0:
                    break
                else:
                    cur.execute("insert into Playeraddress VALUES (%s , %s , %s )",(val[0],val[1],address))
        if ch==3:
            
            if vall[4]> vall[5]:
                try:
                    stri = "SELECT * from TEAM where Tid=" + str(vall[2])
                    cur.execute(stri)
                    stri = cur.fetchone()
                    if len(stri)==0:
                        print("No results found please try again later")
                        return 0
                    stri['W']=stri['W']+1
                    setli=[]
                    setli.append(str(stri['W']))
                    setli.append(str(vall[2]))
                    strin = "UPDATE TEAM SET W= %s WHERE Tid=%s"
                    cur.execute(strin,setli)
                    #print("foof")
                    stri = "SELECT * from TEAM where Tid=" + str(vall[3])
                    cur.execute(stri)
                    #print("flof")
                    stri = cur.fetchone()
                    if len(stri)==0:
                        print("No results found please try again later")
                        return 0
                    stri['L']=stri['L']+1
                    setli=[]
                    setli.append(str(stri['L']))
                    setli.append(str(vall[3]))
                    strin = "UPDATE TEAM SET L= %s WHERE Tid=%s"
                   # print(strin)
                    #strin = "UPDATE TEAM SET L=" + str(stri['L']) + " WHERE Tid="+str(vall[3])
                    cur.execute(strin,setli)
                    con.commit()
                except Exception as e:
                    con.rollback()
                    print("Failed to update number of wins in TeamA the database")
                    print(">>>>>>>>>>>>>", e)
                    return -1
            if vall[4]< vall[5]:
                try:
                    stri = "SELECT * from TEAM where Tid=" + str(vall[3])
                    cur.execute(stri)
                    stri = cur.fetchone()
                    if len(stri)==0:
                        print("No results found please try again later")
                        return 0
                    stri['W']=stri['W']+1
                    setli=[]
                    setli.append(str(stri['W']))
                    setli.append(str(vall[3]))
                    strin = "UPDATE TEAM SET W= %s WHERE Tid=%s"
                    cur.execute(strin,setli)
                    #strin = "UPDATE TEAM SET W=" + str(stri['W']) + " WHERE Tid="+str(vall[3])
                    #cur.execute(strin)
                    stri = "SELECT * from TEAM where Tid=" + str(vall[2])
                    cur.execute(stri)
                    stri = cur.fetchone()
                    if len(stri)==0:
                        print("No results found please try again later")
                        return 0
                    stri['L']=stri['L']+1
                    setli=[]
                    setli.append(str(stri['L']))
                    setli.append(str(vall[2]))
                    strin = "UPDATE TEAM SET L= %s WHERE Tid=%s"
                    cur.execute(strin,setli)
                    #strin = "UPDATE TEAM SET L=" + str(stri['L']) + " WHERE Tid="+str(vall[2])
                    #cur.execute(strin)
                    con.commit()
                except Exception as e:
                    con.rollback()
                    print("Failed to update number of wins TeamB in the database")
                    print(">>>>>>>>>>>>>", e)
                    return -1
            if vall[4] == vall[5]:
                try:
                    stri = "SELECT * from TEAM where Tid=" + str(vall[3])
                    cur.execute(stri)
                    stri = cur.fetchone()
                    if len(stri)==0:
                        print("No results found please try again later")
                        return 0
                    stri['D']=stri['D']+1
                    setli=[]
                    setli.append(str(stri['D']))
                    setli.append(str(vall[3]))
                    strin = "UPDATE TEAM SET D= %s WHERE Tid=%s"
                    cur.execute(strin,setli)
                    # strin = "UPDATE TEAM SET D=" + str(stri['D']) + " WHERE Tid="+str(vall[3])
                    # cur.execute(strin)
                    stri = "SELECT * from TEAM where Tid=" + str(vall[2])
                    cur.execute(stri)
                    stri = cur.fetchone()
                    if len(stri)==0:
                        print("No results found please try again later")
                        return 0
                    stri['D']=stri['D']+1
                    setli=[]
                    setli.append(str(stri['D']))
                    setli.append(str(vall[2]))
                    strin = "UPDATE TEAM SET D= %s WHERE Tid=%s"
                    cur.execute(strin,setli)
                    # strin = "UPDATE TEAM SET D=" + str(stri['D']) + " WHERE Tid="+str(vall[2])
                    # cur.execute(strin)
                    con.commit()
                except Exception as e:
                    con.rollback()
                    print("Failed to update number of wins in the database")
                    print(">>>>>>>>>>>>>", e)
                    return -1            
            
            print("------------Please provide the stats of the players in the current matches--------")
            strin = "SELECT Team , W , L , D from TEAM WHERE Tid="+str(vall[2]) 
            cur.execute(strin)
            var = cur.fetchone()
            if len(var)==0:
                print("No results found please try again later")
                return 0
            print(f"TEAM : {var['Team']} scores:")
            strin = "SELECT * FROM BATSMAN , PLAYER where BATSMAN.passport_number = PLAYER.passport_number AND BATSMAN.player_country = PLAYER.Pcountry "
            cur.execute(strin)
            vari = cur.fetchall()
            if len(vari)==0:
                        print("No results found please try again later")
                        return 0
            for v in vari:
                if v[elist[1][7][0]]==vall[2]:
                    inp=input(str(v[elist[1][2][0]])+ " " +str(v[elist[1][4][0]])+ " : ")
                    try:
                        inp= int(inp)
                        v[elist[5][2][0]]=v[elist[5][2][0]]+inp
                        setli=[]
                        setli.append(v[elist[5][2][0]])
                        setli.append(str(v[elist[1][0][0]]))
                        setli.append(str(v[elist[1][1][0]]))
                        exe="UPDATE BATSMAN SET Number_of_runs = %s WHERE passport_number= %s AND  player_country= %s"
                        cur.execute(exe,setli)
                        tot = int(var['L'])+int(var['W'])+int(var['D'])
                        avg = float(float(v[elist[5][2][0]])/tot)
                        setli=[]
                        setli.append(avg)
                        setli.append(str(v[elist[1][0][0]]))
                        setli.append(str(v[elist[1][1][0]]))
                        exe="UPDATE BATSMAN SET Average_runs = %s WHERE passport_number=%s AND  player_country= %s"
                        cur.execute(exe,setli)
                        setli=[]
                        setli.append(tot)
                        setli.append(str(v[elist[1][0][0]]))
                        setli.append(str(v[elist[1][1][0]]))
                        exe="UPDATE PLAYER SET Matches_played = %s WHERE passport_number=%s AND  Pcountry=%s"
                        cur.execute(exe,setli)
                        con.commit()
                    except Exception as e:
                        con.rollback()
                        print("Failed to update score from the database")
                        print(">>>>>>>>>>>>>", e)
                        return -1
            print(f"TEAM : {var['Team']} wickets:")
            strin = "SELECT * FROM BOWLER , PLAYER where BOWLER.passport_number = PLAYER.passport_number AND BOWLER.player_country = PLAYER.Pcountry "
            cur.execute(strin)
            vari = cur.fetchall()
            if len(vari)==0:
                print("No results found please try again later")
                return 0
            for v in vari:
                if v[elist[1][7][0]]==vall[2]:
                    inp=input(str(v[elist[1][2][0]])+ " " +str(v[elist[1][4][0]])+ " : ")
                    try:
                        inp= int(inp)
                        v[elist[6][2][0]]=v[elist[6][2][0]]+inp
                        setli=[]
                        setli.append(v[elist[6][2][0]])
                        setli.append(str(v[elist[1][0][0]]))
                        setli.append(str(v[elist[1][1][0]]))
                        exe="UPDATE BOWLER SET Number_of_wickets = %s WHERE passport_number= %s AND  player_country= %s"
                        cur.execute(exe,setli)
                        setli=[]
                        setli.append(tot)
                        setli.append(str(v[elist[1][0][0]]))
                        setli.append(str(v[elist[1][1][0]]))
                        exe="UPDATE PLAYER SET Matches_played = %s WHERE passport_number= %s AND  Pcountry=%s"
                        cur.execute(exe,setli)
                        con.commit()
                    except Exception as e:
                        con.rollback()
                        print("Failed to update no of wickets from the database")
                        print(">>>>>>>>>>>>>", e)
                        return -1
                                                   
# ========================================================================================================
                        
                         
            strin = "SELECT Team , W , L , D from TEAM WHERE Tid="+str(vall[3]) 
            cur.execute(strin)
            var = cur.fetchone()
            if len(var)==0:
                print("No results found please try again later")
                return 0
            print(f"TEAM : {var['Team']} scores:")
            strin = "SELECT * FROM BATSMAN , PLAYER where BATSMAN.passport_number = PLAYER . passport_number AND BATSMAN.player_country = PLAYER.Pcountry "
            cur.execute(strin)
            vari = cur.fetchall()
            if len(vari)==0:
                print("No results found please try again later")
                return 0
            for v in vari:
                if v[elist[1][7][0]]==vall[3]:
                    inp=input(str(v[elist[1][2][0]])+ " " +str(v[elist[1][4][0]])+ " : ")
                    try:
                        inp= int(inp)
                        v[elist[5][2][0]]=v[elist[5][2][0]]+inp
                        setli=[]
                        setli.append(v[elist[5][2][0]])
                        setli.append(str(v[elist[1][0][0]]))
                        setli.append(str(v[elist[1][1][0]]))
                        exe="UPDATE BATSMAN SET Number_of_runs = %s WHERE passport_number= %s AND  player_country= %s"
                        cur.execute(exe,setli)
                        tot = int(var['L'])+int(var['W'])+int(var['D'])
                        avg = float(float(v[elist[5][2][0]])/tot)
                        setli=[]
                        setli.append(avg)
                        setli.append(str(v[elist[1][0][0]]))
                        setli.append(str(v[elist[1][1][0]]))
                        exe="UPDATE BATSMAN SET Average_runs = %s WHERE passport_number=%s AND  player_country= %s"
                        cur.execute(exe,setli)
                        setli=[]
                        setli.append(tot)
                        setli.append(str(v[elist[1][0][0]]))
                        setli.append(str(v[elist[1][1][0]]))
                        exe="UPDATE PLAYER SET Matches_played = %s WHERE passport_number=%s AND  Pcountry=%s"
                        cur.execute(exe,setli)
                        con.commit()
                    except Exception as e:
                        con.rollback()
                        print("Failed to update score from the database")
                        print(">>>>>>>>>>>>>", e)
                        return -1
            print(f"TEAM : {var['Team']} wickets:")
            strin = "SELECT * FROM BOWLER , PLAYER where BOWLER.passport_number = PLAYER.passport_number AND BOWLER.player_country = PLAYER.Pcountry "
            cur.execute(strin)
            vari = cur.fetchall()
            if len(vari)==0:
                print("No results found please try again later")
                return 0
            for v in vari:
                if v[elist[1][7][0]]==vall[3]:
                    inp=input(str(v[elist[1][2][0]])+ " " +str(v[elist[1][4][0]])+ " : ")
                    try:
                        inp= int(inp)
                        v[elist[6][2][0]]=v[elist[6][2][0]]+inp
                        setli=[]
                        setli.append(v[elist[6][2][0]])
                        setli.append(str(v[elist[1][0][0]]))
                        setli.append(str(v[elist[1][1][0]]))
                        exe="UPDATE BOWLER SET Number_of_wickets = %s WHERE passport_number= %s AND  player_country= %s"
                        cur.execute(exe,setli)
                        setli=[]
                        setli.append(tot)
                        setli.append(str(v[elist[1][0][0]]))
                        setli.append(str(v[elist[1][1][0]]))
                        exe="UPDATE PLAYER SET Matches_played = %s WHERE passport_number= %s AND  Pcountry=%s"
                        cur.execute(exe,setli)
                        con.commit()
                    except Exception as e:
                        con.rollback()
                        print("Failed to update no of wickets from the database")
                        print(">>>>>>>>>>>>>", e)
                        return -1                            
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
        return -1
    return 

def printattr(ch):
    cnt = 0
    for i in elist[ch-1]:
        cnt = cnt + 1
        print(str(cnt)+"."+ str(i[0]))
    return


def searchintable(ch):
    printattr(ch)
    try:
        ch1 = int(input("Enter choicei> "))
      #  tmp = sp.call('clear', shell=True)
    except:
        print("Sorry the input is not a number!")
        return -1
    fsearch(ch,choosech(ch),ch1)
def fdeletes(ch,namena):
    try:
        strings=""
        print("Please enter the attribute values of the row/rows which you want to DELETE")
        print("INSTRUCTIONS: PRESS ENTER IF YOU DONT WANT TO SELCECT BASED ON THE VALUE OF THE CURRENT ATTRIBUTE")
        cou=0
        couc = len(elist[ch-1])
        cou = 0
        val = {}

        vall={}
        for i in elist[ch-1]:
            if (i[1] == "str"):
                sto=input(i[0]+ " : ")
                if len(sto) == 0:
                    continue
                else:
                    sto = str(sto)
                    vall[i[0]]=sto
            elif i[1] == "int":
                sto=input(i[0]+ " : ")
                if len(sto)==0:
                    continue
                else:
                    sto=float(sto)
                    sto = int(sto)
                    vall[i[0]]=sto
        strings = ""
        couc=len(val)
        cou = 0
        # for i,j in val.items():
        #     cou = cou + 1
        #     if cou <  couc:
        #         strings = strings + str(i)+ "=" + str(j) + " AND "
        #     elif cou==couc:
        #         strings = strings + str(i) + "="+ str(j)+"  "
        string2 = " "
        couc=len(vall)
        cou = 0
        for i,j in vall.items():
            cou = cou + 1
            if cou <  couc:
                string2 = string2 + str(i) + " = "+ "%s"+" AND "
            elif cou==couc:
                string2 = string2 + str(i) +" = "+"%s"+ "  "
        finalstring = "DELETE FROM " + namena + " WHERE " + string2
        values=[]
        for i,j in vall.items():
            values.append(j)
        values = tuple(values)
        # print(finalstring)
        # print(values)
        if (len(values)==0):
            print("No values are specified")
            return -1

        cur.execute(finalstring , values)
        con.commit()
        print("Deleted from Database")
    except Exception as e:
        con.rollback()
        print("Failed to delete from the database")
        print(">>>>>>>>>>>>>", e)
    return

def delete():
    ch=routine([1,2,8,9,10.11,12])
    fdeletes(ch,choosech(ch))
    
def search():
    ch = routine(general)
    searchintable(ch)
    return
           
def doprint(va):
  #  tmp = sp.call('clear', shell=True)
    cnt= 0 
    for i in va:
        cnt = cnt + 1
        if(i == 1):
            print(str(cnt)+". " + choosech(1))
        if(i == 2):
            print(str(cnt)+". " + choosech(2))
        if(i == 3):
            print(str(cnt)+". " + choosech(3))
        if(i == 4):
            print(str(cnt)+". " + choosech(4))
        if(i == 5):
            print(str(cnt)+". " + choosech(5))
        if(i == 6):
            print(str(cnt)+". " + choosech(6))
        if(i == 7):
            print(str(cnt)+". " + choosech(7))
        if(i == 8):
            print(str(cnt)+". " + choosech(8))
        if(i == 9):
            print(str(cnt)+". " + choosech(9))
        if(i == 10):
            print(str(cnt)+". " + choosech(10))
        if(i == 11):
            print(str(cnt)+". " + choosech(11))
        if(i == 12):
            print(str(cnt)+". " + choosech(12))

    return
def routine(va):
    doprint(va)
    try:
     #   print("error somewhere1")
        ch = int(input("Enter choice> "))
      #  tmp = sp.call('clear', shell=True)
      #  print("error somewhere")
        return va[ch-1]
    except:
        print("Sorry the input is not a number!")
    return -1
def choosech(ch):
    if ch==1:
        return "TEAM"
    elif ch==2:
        return "PLAYER"
    elif ch==3:
        return "MATCHES"
    elif ch==4:
        return "VENUE"
    elif ch==5:
        return "STAGE"
    elif ch==6:
        return "BATSMAN"
    elif ch==7:
        return "BOWLER"
    elif ch==8:
        return "COACH"
    elif ch==9:
        return "SPONSOR"
    elif ch==10:
        return "Sponsored_by"
    elif ch==11:
        return "DEPENDENTS"
    elif ch==12:
        return "Playeraddress"
    return
def insert():
    ch=routine([1,2,3,4,5,8,9,10,11,12])
    if ch==-1:
        return
    finsert(ch,choosech(ch))

def fupdate(ch,namena):
    try:
        strings=""
        print("Please enter the attribute values of the row/rows which you want to update GIVE THE CURRENT VALUES")
        print("INSTRUCTIONS: PRESS ENTER IF YOU DONT WANT TO SELCECT BASED ON THE VALUE OF THE CURRENT ATTRIBUTE")
        cou=0
        couc = len(elist[ch-1])
        cou = 0        
        val = {}
        for i in elist[ch-1]:
            if (i[1] == "str"):
                sto=input(i[0]+ " : ")
                if len(sto) == 0:
                    continue
                else:
                    sto = str(sto)
                    val[i[0]]=sto 
            elif i[1] == "int":
                sto=input(i[0]+ " : ")
                if len(sto)==0:
                    continue
                else:
                    sto = float(sto)
                    sto = int(sto)
                    val[i[0]]=sto            
        if(len(val)==0):
            print("No values are specified")
            return -1
        print("Provide the values that you want your selected rows to change to")
        print("INSTRUCTION: PRESS ENTER IF YOU WANT THE VALUE OF THE ATTRIBUTE TO BE THE PREVIOUSLY SET VALUE")
        vall={}
        # print(string2)
        for i in elists[ch-1]:
            if (i[1] == "str"):
                sto=input(i[0]+ " : ")
                if len(sto) == 0:
                    continue
                else:
                    sto = str(sto)
                    vall[i[0]]=sto 
            elif i[1] == "int":
                sto=input(i[0]+ " : ")
                if len(sto)==0:
                    continue
                else:
                    sto = float(sto)
                    sto = int(sto)
                    vall[i[0]]=sto 
        strings = ""
        couc=len(val)
        cou = 0
        for i,j in val.items():
            cou = cou + 1
            if cou <  couc:
                strings = strings + str(i)+ "=" + str(j) + " AND "
            elif cou==couc:
                strings = strings + str(i) + "="+ str(j)+"  "
        string2 = " "
        couc=len(vall)
        cou = 0
        for i,j in vall.items():
            cou = cou + 1
            if cou <  couc:
                string2 = string2 + str(i) + " = "+ "%s"+" , "
            elif cou==couc:
                string2 = string2 + str(i) +" = "+"%s"+ "  "
        finalstring = "UPDATE  " + namena + " SET " + string2 + " WHERE " + strings
        values=[]
        for i,j in vall.items():
            values.append(j)
        values = tuple(values)
        if(len(values) == 0):
            print("No values are specified")
            return -1
        cur.execute(finalstring , values)
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to update the database")
        print(">>>>>>>>>>>>>", e)
    
def fproject(ch,Tablename):
    print("Type Yes or No to project the attributes")
    try:
        val = []
        for i in elist[ch-1]:
            sto=input(i[0]+ " : ")
            sto = str(sto)
            val.append(sto)
        string2="SELECT "
        k=0
        flfl=-1
        for i in val:
            if i.lower()=="yes":
                if string2=="SELECT ":
                    flfl=1
                    string2= string2+ elist[ch-1][k][0]
                else:    
                    string2=string2+" , "+ elist[ch-1][k][0]
            k=k+1
        if flfl==-1:
            print("Nothing is selected please specify something!!")
            return 0
        finalstring= string2 + " FROM " + Tablename
        cur.execute(finalstring)
        vari = cur.fetchall()
        for i in vari:
            for j,k in i.items():
                print(f"{j} : {k}") 
            print("++++++++++++++++++")
    except Exception as e:
        print("Unexpected behaviour")
        print(">>>>>>>>>>>>>", e)
        

def projection():
    ch = routine(general)
    if ch==-1:
        return
    fproject(ch,choosech(ch))
    return

def update():
    ch = routine([1,2,8,9,11,12])
    if ch==-1:
        return
    fupdate(ch,choosech(ch))
        
def selection(): 
   # print("route")
    ch = routine(general)
    tt = 0
    if(ch==2):
        print("------>press 4 if you particularly want a BATSMAN (or)")
        print("------>press 5 if you particularly want a BOWLER (or)")
        print("------>press ENTER if you are not particular")
        tt = (input("Enter choice> "))
        if(len(tt)==0):
            ch = 2
        elif(int(tt) == 4):
            ch = 6
        elif(int(tt) == 5):
            ch = 7
    if ch==1:
        fselect("TEAM")
    elif ch==2:
        fselect("PLAYER")
    elif ch==3:
        fselect("MATCHES")
    elif ch==4:
        fselect("VENUE")
    elif ch==5:
        fselect("STAGE")
    elif ch==6:
        fselect("BATSMAN")
    elif ch==7:
        fselect("BOWLER")
    elif ch==8:
        fselect("COACH")
    elif ch==9:
        fselect("SPONSOR")
    elif ch==10:
        fselect("Sponsored_by")
    elif ch==11:
        fselect("DEPENDENTS")
    elif ch==12:
        fselect("Playeraddress")
    return
     

# def aggregation():
#     ch = routine()
#     return
 

def modification_dispatcher(ch):
    if ch == 1:
        insert()
    elif ch ==2:
        delete()
    elif ch ==3:
        update()
    else:
        print("Option given is invalid")
    return

def functionality_dispatcher(ch):
    if ch==1:
        selection()
    elif ch==2:
        projection()
    elif ch==3:
        aggregation()
    elif ch==4:
        search()
    else:
        print("Option given is invalid")
    return
    
def functionality():
   # tmp = sp.call('clear', shell=True)
    # Here taking example of Employee Mini-world
    print("1. Selection")  # Hire an Employee
    print("2. Projection")  # Fire an Employee
    print("3. Aggregate")  # Promote Employee
    print("4. Search")
    ch = int(input("Enter choice> "))
   # tmp = sp.call('clear', shell=True)
    functionality_dispatcher(ch)
    return 
def modification():
   # tmp = sp.call('clear', shell=True)
    print("1. Insert")
    print("2. Delete")
    print("3. Update")
    ch = int(input("Enter choice> "))
  #  tmp = sp.call('clear', shell=True)
    modification_dispatcher(ch)
    return


def dispatch(ch):
    
    if(ch == 1):
        functionality()
    elif(ch == 2):
        modification()
    elif(ch == 3):
        analysis()
    else:
        print("Error: Invalid Option")
    return

# Global
while(1):
    #tmp = sp.call('clear', shell=True)
    
    wnatto = input("For exiting Program press 1: ")
    if wnatto == "1":
        break
    # Can be skipped if you want to hard core username and password
    username = input("Username: ")
    passwords = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server 
        con = pymysql.connect(host='localhost',
                              user=username,
                              port=5005,
                              password=passwords,
                              db='IPLdb',
                              cursorclass=pymysql.cursors.DictCursor)
        # tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
               # tmp = sp.call('clear', shell=True)
                # Here taking example of Employee Mini-world
                print("1. Functionalities")  # Hire an Employee
                print("2. Modification")  # Fire an Employee
                print("3. Analysis")  # Promote Employee
                print("4. Logout")
                try:
                    ch = int(input("Enter choice> "))
                    # tmp = sp.call('clear', shell=True)
                    if ch == 4:
                        break
                    else:
                        dispatch(ch)
                        tmp = input("Enter any key to CONTINUE>>")
                except:
                    print("Sorry the input is not a number:(")

    except:
       # tmp = sp.call('clear', shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")