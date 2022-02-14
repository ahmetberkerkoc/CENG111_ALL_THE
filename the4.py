

def extract_person(desc):
    family = {}
    for info in desc:
        x = info.split()
        family[x[1]] = ["","","",[],True] #name:  spouse, mother, father, child, alive
        if ("CHILD" in info) or ("MARRIED" in info):
            family[x[2]] = ["","","",[],True]
        if "CHILD" in info:
            for ch in x[3:]:
                family[ch] = ["","","",[],True]
    for info in desc:
        x = info.split()
        if "DEPARTED" in info:
            family[x[1]][-1] = False
        elif "MARRIED" in info:
            family[x[1]][0] = x[2]
            family[x[2]][0] = x[1]
        elif "CHILD" in info:
            family[x[1]][3].extend(x[3:])
            family[x[2]][3].extend(x[3:])
            for ch in x[3:]:
                family[ch][1] = x[1]
                family[ch][2] = x[2]
    return family

def PG1(family,dead,money):
    spouse = family[dead][0]
    child = family[dead][3]
    child_len = len(child)
    inher = {}
    remaining_money = money
    if spouse!="" and family[spouse][-1]:
        remaining_money = money*3/4
        inher[spouse] = money-remaining_money
    
    inher_2=PG1_helper(family,child,remaining_money)
    if len(inher)!=0:
        inher_2[spouse] = inher[spouse]
    return inher_2

def PG1_helper(family,child,money):
    child_len = len(child)
    result_len_child = child_len
    inher = {}
    name = []
    for ch in child:
        if family[ch][-1] == False:
            x = PG1_helper(family,family[ch][3],money/child_len)
            if x == {}:
                child_len -=1
                name.append(ch)
    for ch in child:
        if ch in name:
            continue
        if family[ch][-1]:
            inher[ch] = money/child_len
        else:
            new_inher=PG1_helper(family,family[ch][3],money/child_len)
            for key in new_inher.keys():
                inher[key] = new_inher[key]
            

    return inher
    
    
def PG2(family,dead,money):
    spouse = family[dead][0]
    father = family[dead][2]
    mother = family[dead][1]
    inher = {}
    if mother=="" and father=="":
        return inher
    remaining_money = money
    if spouse!="" and family[spouse][-1]:
        remaining_money = money*2/4
        inher[spouse] = money-remaining_money
    if family[father][-1] and family[mother][-1]:
        inher[father] = remaining_money/2
        inher[mother] = remaining_money/2
    elif family[father][-1]:
        m_child=[]
        for i in family[mother][3]:
            if i == dead:
                continue
            m_child.append(i)
        y=PG1_helper(family,m_child,remaining_money/2)
        if y=={}:
            inher[father] = remaining_money
        else:
            inher[father] = remaining_money/2
        for key in y.keys():
            inher[key] = y[key]
    
    elif family[mother][-1]:
        m_child=[]
        for i in family[father][3]:
            if i == dead:
                continue
            m_child.append(i)
        y=PG1_helper(family,m_child,remaining_money/2)
        if y=={}:
            inher[mother] = remaining_money
        else:
            inher[mother] = remaining_money/2
        for key in y.keys():
            inher[key] = y[key]
    else:
        m_child=[]
        f_child = [] 
        for i in family[father][3]:
            if i == dead:
                continue
            f_child.append(i)
        for i in family[mother][3]:
            if i == dead:
                continue
            m_child.append(i)
        f=PG1_helper(family,f_child,remaining_money/2)
        m=PG1_helper(family,m_child,remaining_money/2)
        for key in f.keys():
                inher[key] = f[key]
        for key in m.keys():
                if key in inher.keys():
                   inher[key] = inher[key]+m[key]
                else: 
                    inher[key] = m[key]    
    return inher
 
def PG3(family,dead,money):
    spouse = family[dead][0]
    mother = family[dead][1]
    father = family[dead][2]
    inher={}
    if mother=="" and father=="":
        return inher
    mother_mother  = family[mother][1] 
    mother_father = family[father][1] 
    father_mother = family[mother][2] 
    father_father = family[father][2] 
    if mother_father=="" and father_father=="" and mother_mother=="" and father_mother=="":
        return inher
    mm={}
    ff={}
    mf={}
    fm={}
    divisor = 4
    if mother_father=="":
        divisor -=1
    if mother_mother=="":
        divisor -=1
    if father_mother=="":
        divisor -=1
    if father_father=="":
        divisor -=1
    remaining_money = money 
    if spouse!="" and family[spouse][-1]:
        remaining_money = money*1/4
        inher[spouse] = money-remaining_money
    if mother_mother !="":    
        if family[mother_mother][-1]:
            mm[mother_mother]=remaining_money/divisor
        else:
            mm_child = family[mother_mother][3]
            mm = PG1_helper(family, mm_child,remaining_money/divisor)
            if mm =={}:
                divisor -=1
    if father_mother!="":
        if family[father_mother][-1]:
            fm[father_mother]=remaining_money/divisor
        else:
            fm_child = family[father_mother][3]
            fm = PG1_helper(family, fm_child,remaining_money/divisor)
            if fm =={}:
                divisor -=1
    if mother_father!="":
        if family[mother_father][-1]:
            mf[mother_father]=remaining_money/divisor
        else:
            mf_child = family[mother_father][3]
            mf = PG1_helper(family, mf_child,remaining_money/divisor)
            if mf =={}:
                divisor -=1
    if father_father!="":    
        if family[father_father][-1]:
            ff[father_father]=remaining_money/divisor
        else:
            ff_child = family[father_father][3]
            ff = PG1_helper(family, ff_child,remaining_money/divisor)
            if ff =={}:
                divisor -=1
    combined = combine_dic(mm,mf,fm,ff)
    if spouse !="":
        combined[spouse] = inher[spouse]
    return combined

def combine_dic(mm,mf,fm,ff):
    combined = {}
    for key in mm.keys():
        combined[key]=mm[key]
    for key in mf.keys():
        if key in combined.keys():
            combined[key] = combined[key] + mf[key]
        else:
            combined[key] =  mf[key]
    for key in fm.keys():
        if key in combined.keys():
            combined[key] = combined[key] + fm[key]
        else:
            combined[key] =  fm[key]
    for key in ff.keys():
        if key in combined.keys():
            combined[key] = combined[key] + ff[key]
        else:
            combined[key] =  ff[key]
    return combined
def print_inher(inher):
    lst=[]
    for name in inher:
        lst.append((name,inher[name]))
    return lst


def inheritance(Descriptions):
    news = Descriptions[-1].split()
    dead = news[1]
    
    money = float(news[2])
    
    family = extract_person(Descriptions[:-1])
    spouse = family[dead][0]
    inher=PG1(family,dead,money)
    if inher == {} or (len(inher)==1 and (spouse in inher.keys())):
        inher = PG2(family,dead,money)
    if inher == {} or (len(inher)==1 and (spouse in inher.keys())):
        inher=PG3(family,dead,money)
    if inher == {} or (len(inher)==1 and (spouse in inher.keys())):
        if spouse !="" and family[spouse][-1]==True:
            inher[spouse] = money
    lst_inher = print_inher(inher)
    return lst_inher