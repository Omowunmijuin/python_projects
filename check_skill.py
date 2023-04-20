#!/usr/bin/python3
'''program that uses sets to check for candidate skills'''


skills = {'Python', 'HTML', 'SQL', 'C++', 'Java', 'Scala'}
job_skills = {'HTML', 'CSS', 'JS', 'C#', 'NodeJS'}

candidateSkills = (job_skills & skills)
for s in candidateSkills:
    print(str(s))
