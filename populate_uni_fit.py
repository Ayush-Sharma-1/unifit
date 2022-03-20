import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'unifit.settings')

import django
django.setup()

from uni_fit.models import University, University_Department, Reddit #<--need to check if this is added
from uni_fit.models import Users

def populate():

    universities = {
                    'Massachusetts Institute of Technology':	{'UniName':'Massachusetts Institute of Technology',	'Country':'US',	'UniRank':'1',	'About':'The Massachusetts Institute of Technology is a private land-grant research university in Cambridge, Massachusetts. Established in 1861, MIT has since played a key role in the development of modern technology and science, ranking it among the top academic institutions in the world.',	'Link':'https://web.mit.edu/'},
                    'University of Oxford':	{'UniName':'University of Oxford',	'Country':'UK',	'UniRank':'2',	'About':'The University of Oxford is a collegiate research university in Oxford, England. There is evidence of teaching as early as 1096, making it the oldest university in the English-speaking world and the world\'\s second-oldest university in continuous operation. ',	'Link':'https://www.ox.ac.uk/'},
                    'Standford University':	{'UniName':'Standford University',	'Country':'US',	'UniRank':'3',	'About':'Stanford University, officially Leland Stanford Junior University, is a private research university in Stanford, California. The campus occupies 8,180 acres, among the largest in the United States, and enrolls over 17,000 students. Stanford is ranked among the best universities in the world.',	'Link':'https://www.stanford.edu/'},
                    'University of Cambridge':	{'UniName':'University of Cambridge',	'Country':'UK',	'UniRank':'4',	'About':'The University of Oxford is a collegiate research university in Oxford, England. There is evidence of teaching as early as 1096, making it the oldest university in the English-speaking world and the world\'\s second-oldest university in continuous operation. ',	'Link':'https://www.ox.ac.uk/'},
                    'Harvard University':	{'UniName':'Harvard University',	'Country':'US',	'UniRank':'5',	'About':'Harvard University is a private Ivy League research university in Cambridge, Massachusetts. Founded in 1636 as Harvard College and named for its first benefactor, the Puritan clergyman John Harvard, it is the oldest institution of higher learning in the United States and among the most prestigious in the world.',	'Link':'https://www.harvard.edu/'},
                    'California Institute of Technology':	{'UniName':'California Institute of Technology',	'Country':'US',	'UniRank':'6',	'About':'The California Institute of Technology is a private research university in Pasadena, California, United States of America.',	'Link':'https://www.caltech.edu/'},
                    'UCL':	{'UniName':'UCL',	'Country':'UK',	'UniRank':'8',	'About':'University College London, which operates as UCL, is a major public research university located in London, United Kingdom. UCL is a member institution of the federal University of London, and is the second-largest university in the United Kingdom by total enrolment and the largest by postgraduate enrolment.',	'Link':'https://www.ucl.ac.uk/'},
                    'Princeton University':	{'UniName':'Princeton University',	'Country':'US',	'UniRank':'20',	'About':'Princeton University is a private Ivy League research university in Princeton, New Jersey. Founded in 1746 in Elizabeth as the College of New Jersey, Princeton is the fourth-oldest institution of higher education in the United States and one of the nine colonial colleges chartered before the American Revolution.',	'Link':'https://www.princeton.edu/'},
                    'University of Toronto':	{'UniName':'University of Toronto',	'Country':'Canada',	'UniRank':'26',	'About':'The University of Toronto, known more specifically as the University of Toronto St. George, is a public research university in Toronto, Ontario, Canada, located on the grounds that surround Queen\'\s Park.',	'Link':'https://www.utoronto.ca/'},
                    'McGill University':	{'UniName':'McGill University',	'Country':'Canada',	'UniRank':'27',	'About':'McGill University (French: Université McGill) is an English-language public research university located in Montreal, Quebec, Canada. Founded in 1821 by royal charter granted by King George IV,[9] the university bears the name of James McGill, a Scottish merchant whose bequest in 1813 formed the university\'\s precursor, University of McGill College (or simply, McGill College); the name was officially changed to McGill University in 1885.',	'Link':'https://www.mcgill.ca/'},
                    'Austrailian National University':	{'UniName':'Austrailian National University',	'Country':'Austrailia',	'UniRank':'28',	'About':'The Australian National University is a public research university located in Canberra, the capital of Australia. Its main campus in Acton encompasses seven teaching and research colleges, in addition to several national academies and institutes. ',	'Link':'https://www.anu.edu.au/'},
                    'University of Melbourne':	{'UniName':'University of Melbourne',	'Country':'Austrailia',	'UniRank':'37',	'About':'The University of Melbourne is a public research university located in Melbourne, Australia. Founded in 1853, it is Australia\'\s second oldest university and the oldest in Victoria.',	'Link':'https://www.unimelb.edu.au/'},
                    'University of Sydney':	{'UniName':'University of Sydney',	'Country':'Austrailia',	'UniRank':'38',	'About':'The University of Sydney is a public research university located in Sydney, Australia. Founded in 1850 as Australia\'\s first university, it is regarded as one of the world\'\s leading universities. The university is one of Australia\'\s six sandstone universities.',	'Link':'https://www.sydney.edu.au/'},
                    'University of New South Wales':	{'UniName':'University of New South Wales',	'Country':'Austrailia',	'UniRank':'43',	'About':'The University of New South Wales, also known as UNSW Sydney, is a public research university based in Sydney, New South Wales, Australia. It is one of the founding members of Group of Eight, a coalition of Australian research-intensive universities.',	'Link':'https://www.unsw.edu.au/'},
                    'University of British Columbia':	{'UniName':'University of British Columbia',	'Country':'Canada',	'UniRank':'46',	'About':'The University of British Columbia is a public research university with campuses near Vancouver and in Kelowna, British Columbia. Established in 1908, UBC is British Columbia\'\s oldest university. The university ranks among the top three universities in Canada.',	'Link':'https://www.ubc.ca/'},
                    'University of Queensland':	{'UniName':'University of Queensland',	'Country':'Austrailia',	'UniRank':'47',	'About':'The University of Queensland is a public research university located primarily in Brisbane, the capital city of the Australian state of Queensland. Founded in 1909 by the Queensland parliament, UQ is one of the six sandstone universities, an informal designation of the oldest university in each state. ',	'Link':'https://www.uq.edu.au/'},
                    'Institut Polytechnique de Paris ':	{'UniName':'Institut Polytechnique de Paris ',	'Country':'France',	'UniRank':'49',	'About':'The Polytechnic Institute of Paris is a research university system located in Palaiseau, France. It consists of five engineering schools: Télécom Paris, Télécom SudParis, ENSTA Paris, ENSAE ParisTech, and École Polytechnique.',	'Link':'https://www.ip-paris.fr/en'},
                    'Université PSL (Paris Sciences & Lettres)':	{'UniName':'Université PSL (Paris Sciences & Lettres)',	'Country':'France',	'UniRank':'52',	'About':'Paris Sciences et Lettres University is a public research university in Paris, France. It was established in 2010 and formally created as a university in 2019. It is a collegiate university with 11 constituent schools.',	'Link':'https://psl.eu/en'},
                    'Ecole Polytechnique':	{'UniName':'Ecole Polytechnique',	'Country':'France',	'UniRank':'68',	'About':'The École Polytechnique is one of the most prestigious and selective grandes écoles in France. It is a French public institution of higher education and research in Palaiseau, a suburb south of Paris. The school is a constituent member of the Polytechnic Institute of Paris.',	'Link':'https://www.polytechnique.edu/en'},
                    'Univeristy of Glasgow':	{'UniName':'Univeristy of Glasgow',	'Country':'UK',	'UniRank':'73',	'About':'The University of Glasgow is a public research university in Glasgow, Scotland. Founded by papal bull in 1451, it is the fourth-oldest university in the English-speaking world and one of Scotland\'\s four ancient universities',	'Link':'https://www.gla.ac.uk/'},
                    'Sorbonne University':	{'UniName':'Sorbonne University',	'Country':'France',	'UniRank':'83',	'About':'The University of Paris, metonymically known as the Sorbonne, was the main university in Paris, France, active from 1150 to 1970, with the exception of 1793–1806 under the French Revolution.',	'Link':'https://www.sorbonne-universite.fr/en'},
                    'CentraleSupélec':	{'UniName':'CentraleSupélec',	'Country':'France',	'UniRank':'138',	'About':'CentraleSupélec is a top French graduate engineering school of Paris-Saclay University in Gif-sur-Yvette, France. It was established on 1 January 2015, as a result of a strategic merger between two prestigious grandes écoles in France, École Centrale Paris and Supélec. ',	'Link':'https://www.centralesupelec.fr/'},
                    'University of Exeter':	{'UniName':'University of Exeter',	'Country':'UK',	'UniRank':'149',	'About':'The University of Exeter is a public research university in Exeter, Devon, South West England, United Kingdom. Its predecessor institutions, St Luke\'\s College, Exeter School of Science, Exeter School of Art, and the Camborne School of Mines were established in 1838, 1855, 1863, and 1888 respectively.',	'Link':'https://www.exeter.ac.uk/'},
                    'University of Waterloo':	{'UniName':'University of Waterloo',	'Country':'Canada',	'UniRank':'149',	'About':'The University of Waterloo is a public research university with a main campus in Waterloo, Ontario, Canada. The main campus is on 404 hectares of land adjacent to "Uptown" Waterloo and Waterloo Park. The university also operates three satellite campuses and four affiliated university colleges.',	'Link':'https://uwaterloo.ca/'},
                    'Simon Fraser University':	{'UniName':'Simon Fraser University',	'Country':'Canada',	'UniRank':'298',	'About':'Simon Fraser University is a public research university in British Columbia, Canada, with three campuses: Burnaby, Surrey, and Vancouver.',	'Link':'https://www.sfu.ca/'}}
                    

    University_Departments = {
                '1':	{'UniId':'1',	'DeptName':'Engineering',	'DeptRank':'1',	'Link':'https://engineering.mit.edu/'},
                '2':	{'UniId':'2',	'DeptName':'Engineering',	'DeptRank':'2',	'Link':'https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/engineering-science'},
                '3':	{'UniId':'3',	'DeptName':'Engineering',	'DeptRank':'3',	'Link':'https://engineering.stanford.edu/'},
                '4':	{'UniId':'4',	'DeptName':'Engineering',	'DeptRank':'4',	'Link':'https://www.undergraduate.study.cam.ac.uk/courses/engineering'},
                '5':	{'UniId':'5',	'DeptName':'Engineering',	'DeptRank':'5',	'Link':'https://www.seas.harvard.edu/'},
                '6':	{'UniId':'6',	'DeptName':'Engineering',	'DeptRank':'6',	'Link':'https://eas.caltech.edu/'},
                '7':	{'UniId':'7',	'DeptName':'Engineering',	'DeptRank':'8',	'Link':'https://www.ucl.ac.uk/prospective-students/undergraduate/degrees?query=Engineering&p0='},
                '8':	{'UniId':'8',	'DeptName':'Engineering',	'DeptRank':'20',	'Link':'https://www.princeton.edu/academics/areas-of-study/engineering'},
                '9':	{'UniId':'9',	'DeptName':'Engineering',	'DeptRank':'26',	'Link':'https://www.utoronto.ca/academics/programs-directory?field_degrees_value=1&query=+Engineering'},
                '10':	{'UniId':'10',	'DeptName':'Engineering',	'DeptRank':'27',	'Link':'https://www.mcgill.ca/undergraduate-admissions/programs?f%5B0%5D=field_areas_interest%3A20'},
                '11':	{'UniId':'11',	'DeptName':'Engineering',	'DeptRank':'28',	'Link':'https://programsandcourses.anu.edu.au/degree-builder/area-of-interest?career=undergraduate&areaOfInterest=engineering'},
                '12':	{'UniId':'12',	'DeptName':'Engineering',	'DeptRank':'37',	'Link':'https://study.unimelb.edu.au/find/'},
                '13':	{'UniId':'13',	'DeptName':'Engineering',	'DeptRank':'38',	'Link':'https://www.sydney.edu.au/courses/search.html?keywords=engineering&search-type=course&course-level=uc&page=1'},
                '14':	{'UniId':'14',	'DeptName':'Engineering',	'DeptRank':'43',	'Link':'https://www.unsw.edu.au/study/find-a-degree-or-course/degree-search-results#search=Engineering&sort=relevance&startRank=1&numRanks=12'},
                '15':	{'UniId':'15',	'DeptName':'Engineering',	'DeptRank':'46',	'Link':'https://you.ubc.ca/programs/#mode=by-topic&viewMode=list&filters[search]=Engineering'},
                '16':	{'UniId':'16',	'DeptName':'Engineering',	'DeptRank':'47',	'Link':'https://future-students.uq.edu.au/study/programs?search=engineering&year=2022'},
                '17':	{'UniId':'17',	'DeptName':'Engineering',	'DeptRank':'49',	'Link':'https://www.ip-paris.fr/en/topics/engineer-programs'},
                '18':	{'UniId':'18',	'DeptName':'Engineering',	'DeptRank':'52',	'Link':'https://psl.eu/formations?field_discipline=Engineering%20Science%20(225)'},
                '19':	{'UniId':'19',	'DeptName':'Engineering',	'DeptRank':'68',	'Link':'https://programmes.polytechnique.edu/en/bachelor/bachelor-of-science'},
                '20':	{'UniId':'20',	'DeptName':'Engineering',	'DeptRank':'73',	'Link':'https://www.gla.ac.uk/schools/engineering/'},
                '21':	{'UniId':'21',	'DeptName':'Engineering',	'DeptRank':'83',	'Link':'https://sciences.sorbonne-universite.fr/formation-sciences/offre-de-formation-par-discipline'},
                '22':	{'UniId':'22',	'DeptName':'Engineering',	'DeptRank':'138',	'Link':'https://www.centralesupelec.fr/en/engineering-curriculum'},
                '23':	{'UniId':'23',	'DeptName':'Engineering',	'DeptRank':'149',	'Link':'https://www.exeter.ac.uk/undergraduate/courses/engineering/'},
                '24':	{'UniId':'24',	'DeptName':'Engineering',	'DeptRank':'149',	'Link':'https://uwaterloo.ca/future-students/missing-manual/applying/how-choose-program-faculty-engineering'},
                '25':	{'UniId':'25',	'DeptName':'Engineering',	'DeptRank':'298',	'Link':'https://www.sfu.ca/students/admission/programs/a-z/e/engineering-science/overview.html'}
}
                


    reddit = {
                'University of Oxford':	{'UniName':'University of Oxford',	'SubReddit':'r/oxforduni',	'Link':'https://www.reddit.com/r/oxforduni/'},
                'Stanford University':	{'UniName':'Stanford University',	'SubReddit':'r/stanford',	'Link':'https://www.reddit.com/r/stanford/'},
                'Harvard University':	{'UniName':'Harvard University',	'SubReddit':'r/Harvard',	'Link':'https://www.reddit.com/r/Harvard/'},
                'California Institute of Technology':	{'UniName':'California Institute of Technology',	'SubReddit':'r/Caltech',	'Link':'https://www.reddit.com/r/Caltech/'},
                'University College London':	{'UniName':'University College London',	'SubReddit':'r/UCL',	'Link':'https://www.reddit.com/r/UCL/'},
                'Princeton University':	{'UniName':'Princeton University',	'SubReddit':'r/princeton',	'Link':'https://www.reddit.com/r/princeton/'},
                'University of Toronto':	{'UniName':'University of Toronto',	'SubReddit':'r/UofT',	'Link':'https://www.reddit.com/r/UofT/'},
                'McGill University ':	{'UniName':'McGill University ',	'SubReddit':'r/mcgill',	'Link':'https://www.reddit.com/r/mcgill/'},
                'Australian National University':	{'UniName':'Australian National University',	'SubReddit':'r/Anu',	'Link':'https://www.reddit.com/r/Anu/'},
                'University of Melbourne':	{'UniName':'University of Melbourne',	'SubReddit':'r/unimelb',	'Link':'https://www.reddit.com/r/unimelb/'},
                'University of Sydney':	{'UniName':'University of Sydney',	'SubReddit':'r/usyd',	'Link':'https://www.reddit.com/r/usyd/'},
                'University of New South Wales':	{'UniName':'University of New South Wales',	'SubReddit':'r/unsw',	'Link':'https://www.reddit.com/r/unsw/'},
                'The University of British Columbia':	{'UniName':'The University of British Columbia',	'SubReddit':'r/UBC',	'Link':'https://www.reddit.com/r/UBC/'},
                'The University of Queensland':	{'UniName':'The University of Queensland',	'SubReddit':'r/Uqreddit',	'Link':'https://www.reddit.com/r/UQreddit/'},
                'Polytechnic Institute of Paris':	{'UniName':'Polytechnic Institute of Paris',	'SubReddit':'r/france',	'Link':'https://www.reddit.com/r/france/'},
                'Paris Sciences et Lettres University':	{'UniName':'Paris Sciences et Lettres University',	'SubReddit':'r/PSLUniversity',	'Link':'https://www.reddit.com/r/PSLUniversity/'},
                'The École polytechnic':	{'UniName':'The École polytechnic',	'SubReddit':'r/france',	'Link':'https://www.reddit.com/r/france/'},
                'University of Glasgow':	{'UniName':'University of Glasgow',	'SubReddit':'r/GlasgowUni',	'Link':'https://www.reddit.com/r/GlasgowUni/'},
                'University of Paris':	{'UniName':'University of Paris',	'SubReddit':'r/france',	'Link':'https://www.reddit.com/r/france/'},
                'Centrale Supélec':	{'UniName':'Centrale Supélec',	'SubReddit':'r/france',	'Link':'https://www.reddit.com/r/france/'},
                'University of Exeter':	{'UniName':'University of Exeter',	'SubReddit':'r/exeter',	'Link':'https://www.reddit.com/r/exeter/'},
                'University of Waterloo':	{'UniName':'University of Waterloo',	'SubReddit':'r/uwaterloo',	'Link':'https://www.reddit.com/r/uwaterloo/'},
                'Simon Fraser University ':	{'UniName':'Simon Fraser University ',	'SubReddit':'r/simonfraser',	'Link':'https://www.reddit.com/r/simonfraser/'}
    }


    for UniName, uni_data in universities.items():
        u = add_University(uni_data['UniName'], uni_data['Country'], uni_data['UniRank'], uni_data['About'], uni_data['Link'])

    for u in University.objects.all():
        return u


    for UniId, uni_data in University_Departments.items():
        ud = add_universityDepartment(UniId, uni_data['DeptName'], uni_data['DeptRank'],uni_data['Link'])

    for ud in University_Department.objects.all():
        return ud
    

    for UniName, reddit_data in reddit.items():
        r = add_Reddit(UniName, reddit_data['SubReddit'], reddit_data['Link'])

    for r in Reddit.objects.all():
        return r
       
      

def add_University( UniName, Country, UniRank, About, Link):
    u = University.objects.get_or_create(UniRank=UniRank,Country=Country,UniName=UniName,About=About,Link=Link)
   # u.save()
    #return u


def add_universityDepartment(UniId,DeptName, DeptRank, Link):
    ud = University_Department.object.get_or_create()
    ud.UniId=UniId
    ud.DeptName=DeptName
    ud.DeptRank=DeptRank
    ud.Link=Link
    ud.save()
    return ud


def add_Reddit(SubReddit, Link, UniName):
    r = Reddit.objects.get_or_create(UniName,SubReddit,Link)
    r.SubReddit=SubReddit
    r.Link=Link
    r.UniName=UniName
    r.save()
    return r


if __name__ == '__main__' :
    print("Starting unifit Rango Population script...")
    populate()
