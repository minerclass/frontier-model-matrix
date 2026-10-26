import json, csv
S={
'gcard':('https://deepmind.google/models/model-cards/gemini-4-argon/','2026-10-13','Google DeepMind Gemini 4 Argon model card'),
'gblog':('https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/','2026-10-13','Google blog: Gemini 4 Argon available'),
'aa_argon':('https://artificialanalysis.ai/articles/gemini-4-argon-google-top-three-labs','2026-09-30','Artificial Analysis: Gemini 4 Argon'),
'aa_fable':('https://artificialanalysis.ai/articles/claude-fable-5-1','2026-09-01','Artificial Analysis: Claude Fable 5.1'),
'aa_grok':('https://artificialanalysis.ai/articles/benchmarking-grok-4-7','2026-09-21','Artificial Analysis: Benchmarking Grok 4.7'),
'aa_muse':('https://artificialanalysis.ai/articles/muse-wonder','2026-10-12','Artificial Analysis: Muse Wonder'),
'aa_astra':('https://artificialanalysis.ai/articles/benchmarking-gpt-6-astra','2026-09','Artificial Analysis: Benchmarking GPT-6 Astra (via search summary)'),
'anth_opus':('https://www.anthropic.com/claude/opus','2026-09-22','Anthropic Claude Opus 5.5 page'),
'opus_docs':('https://platform.claude.com/docs/en/models/opus-5-5/overview.md','2026-09-22','Claude Opus 5.5 docs'),
'bh_swepro':('https://benchmarkheaven.com/benchmarks/result?axis=anthropic-swe-bench-pro%3A%3Asnapshot-2026-09-22%40%40Vendor-reported%2520by%2520Anthropic%40%40percent&model=claude-opus-5.5%3A%3Amax','2026-09-22','Benchmark Heaven citing Opus 5.5 system card'),
'bl_opus':('https://benchmarklist.com/models/anthropic-claude-opus-5.5/','2026-09-28','BenchmarkList citing Opus 5.5 system card'),
'oai_sol':('https://openai.com/index/introducing-gpt-6-1-sol/','2026-09-29','OpenAI: Introducing GPT-6.1 Sol'),
'oai_sc':('https://deploymentsafety.openai.com/gpt-6-1-sol/introduction','2026-09-29','OpenAI GPT-6.1 Sol system card addendum'),
'bl_sol':('https://benchmarklist.com/models/openai-gpt-6.1-sol/','2026-09-29','BenchmarkList citing OpenAI GPT-6.1 Sol launch charts'),
'xai':('https://x.ai/news/grok-4-7','2026-09-21','SpaceXAI: Introducing Grok 4.7'),
'apidog_grok':('https://apidog.com/blog/grok-4-7-benchmarks/','2026-09','Apidog: Grok 4.7 benchmarks and SWE-Together'),
'meta_dev':('https://dev.meta.ai/resources/blog/build-with-muse-wonder','2026-10-12','Meta: Build with Muse Wonder'),
'tot_muse':('https://www.tokensortowers.com/us/models/muse-wonder-full','2026-10-12','Tokens or Towers citing Meta and AA'),
'benchlm_muse':('https://benchlm.ai/models/muse-wonder-full','2026-10-12','BenchLM citing Meta model card and AA'),
'aa_kimi':('https://artificialanalysis.ai/articles/kimi-k3-1-pro-launch-benchmarks','2026-10-23','Artificial Analysis: Kimi K3.1 Pro launches at 4th on the Intelligence Index'),
'aa_health':('https://artificialanalysis.ai/articles/healthbench-professional-health-conversations','2026-10-19','Artificial Analysis: HealthBench and HealthBench Professional leaderboards'),
'aa_fcode':('https://artificialanalysis.ai/articles/frontiercode','2026-10-12','Artificial Analysis: FrontierCode 1.1 launch article'),
'aa_decision':('https://artificialanalysis.ai/articles/artificial-analysis-decision-index','2026-10-13','Artificial Analysis: Decision Index v1.0 launch article'),
'aa_robotics':('https://artificialanalysis.ai/articles/aa-robotics','2026-10-14','Artificial Analysis: AA-Robotics v0.1'),
'aa_3d':('https://artificialanalysis.ai/articles/aa-3d','2026-10-12','Artificial Analysis: AA-3D launch article'),
'aa_beam':('https://artificialanalysis.ai/articles/reflection-beam','2026-10-16','Artificial Analysis: Reflection Beam (cites Muse Spark Open index score)'),
'arena_text':('https://arena.ai/leaderboard/text','2026-10-22','Arena (formerly LMArena) Text leaderboard, overall'),
'meta_sparkopen':('https://dev.meta.ai/models/muse-spark-open/','2026-10-15','Meta: Muse Spark Open model page (benchmark table)'),
'meta_sparkopen_blog':('https://dev.meta.ai/resources/blog/build-with-muse-spark-open','2026-10-15','Meta: Build with Muse Spark Open'),
'meta_spark13':('https://research.meta.ai/blog/introducing-muse-spark-1-3','2026-09-02','Meta AI Research: Introducing Muse Spark 1.3'),
'anth_news':('https://www.anthropic.com/news','2026-10-26','Anthropic newsroom (release dates for Sonnet 5.5 and Haiku 5.5)'),
'kimi_blog':('https://www.kimi.ai/blog/kimi-k3-1-pro','2026-10-23','Moonshot AI: Kimi K3.1 Pro tech blog'),
}
M=[ # id,name,maker,family,release,status,note
('argon','Gemini 4 Argon','Google','Gemini 4','2026-10-13','verified','GA Oct 13 per Google blog; AA tested a limited rollout Sep 30. Effort: high (highest available).'),
('astra','GPT-6 Astra','OpenAI','GPT-6','2026-09-03','verified','Release date from search summary of OpenAI/AA pages. No "GPT-6.1 Astra" found.'),
('sol61','GPT-6.1 Sol','OpenAI','GPT-6.1','2026-09-29','verified','Only GPT-6.1 model found. Matches the user\'s "ChatGPT 6.1".'),
('sol6','GPT-6 Sol','OpenAI','GPT-6','2026-09-22','verified','Predecessor of 6.1 Sol.'),
('luna','GPT-6 Luna','OpenAI','GPT-6',None,'partial','Named in OpenAI system card; release date still not verified. Independent figures added 2026-10-26 (AA HealthBench, FrontierCode, Decision Index; Arena).'),
('opus55','Claude Opus 5.5','Anthropic','Claude 5.5','2026-09-22','verified',''),
('sonnet55','Claude Sonnet 5.5','Anthropic','Claude 5.5','2026-09-28','partial','Release date Sep 28, 2026 per Anthropic newsroom (read 2026-10-26). Independent figures only; no Anthropic benchmark claims collected.'),
('haiku55','Claude Haiku 5.5','Anthropic','Claude 5.5','2026-10-07','partial','Release date Oct 7, 2026 per Anthropic newsroom (read 2026-10-26). Independent figures only (AA Decision Index, Arena).'),
('fable51','Claude Fable 5.1','Anthropic','Claude Fable','2026-09-01','verified',''),
('grok47','Grok 4.7','SpaceXAI (xAI)','Grok 4.7','2026-09-21','verified','Variants low/high/xhigh. No Cursor-specific Grok 4.7 model found; xAI reports CursorBench 4.0.'),
('wfull','Muse Wonder Full','Meta','Muse Wonder','2026-10-12','verified','Muse Code subscription only.'),
('wonder','Muse Wonder','Meta','Muse Wonder','2026-10-12','verified','API $4/$20.'),
('spark13','Muse Spark 1.3','Meta','Muse Spark','2026-09-02','partial','Release date Sep 2, 2026 per Meta AI Research blog (read 2026-10-26).'),
('sparkopen','Muse Spark Open','Meta','Muse Spark','2026-10-15','verified','New 2026-10-26. Open-weight 816B total / 42B active, derived from Muse Spark (Aug 2026). Meta table setting: xhigh.'),
('kimi31','Kimi K3.1 Pro','Moonshot AI','Kimi K3.1','2026-10-23','verified','New entrant added 2026-10-26. API launch Oct 23, 2026 (Moonshot blog and AA article); weights promised by Nov 4, 2026. 2.8T total / 104B active.'),
]
R=[]
def r(m,b,v,t,rep,src,setting='',note='',unit='%'):
    R.append(dict(model=m,benchmark=b,value=v,unit=unit,type=t,reporter=rep,setting=setting,note=note,source_key=src,source=S[src][0],date=S[src][1]))
G=[('Vals Index',68.9,63.1,65.8,67.0),('AutomationBench (Zapier)',51.3,41.4,31.4,42.5),('Vals Finance Agent v2',65.4,53.5,58.9,58.6),('Harvey Legal Agent',19.6,5.4,6.7,3.8),('DeepSWE v1.1',77.9,74.1,67.4,74.2),('FrontierSWE v2',55.0,65.5,56.3,62.3),('Vibe Code Bench',91.9,89.6,90.3,90.3),('Terminal-Bench 4.0',57.4,58.2,57.9,66.4),('PostTrainBench',45.3,44.3,40.2,49.3),('Terminal-Bench Science 0.1',57.6,68.1,52.6,63.3),('LABBench 2',88.8,85.4,68.6,73.1),('RiemannBench',76.0,72.0,65.6,69.6),('GraphWalks <=128k',99.7,98.7,91.4,90.6),('GraphWalks 256k-1M',84.2,71.8,65.0,66.8),("Agent's Last Exam",39.5,34.2,None,38.2),('OSWorld-2.0 offline (partial)',69.2,72.6,None,None),('Chartography',71.6,71.0,46.2,66.3),('LVBench',91.7,87.5,79.7,83.7),('CWE-bench v1',68.0,68.0,58.0,67.0)]
GB=[g[0] for g in G]
for row in G:
    b=row[0]
    for m,v in zip(['argon','astra','fable51','opus55'],row[1:]):
        if v is None: continue
        r(m,b,v,'claim' if m=='argon' else 'vendor-table','Google',"gcard",'Google launch table',"Rival values come from public leaderboards, Google runs, or rival system cards; harness differs by row (Apidog analysis)." if m!='argon' else '9 of 19 rows sourced from public leaderboards per Apidog.')
r('argon','ERQA',87,'claim','Google','gblog','pure reasoning')
r('opus55','SWE-bench Pro',89.9,'claim','Anthropic','bh_swepro','adaptive thinking max, default fallback','Best independent SWE-bench Pro result (Scale) reported at 61.5 for a different model (LLMLearner).')
r('opus55','Terminal-Bench 4.0',66.4,'claim','Anthropic','anth_opus','xhigh effort, SE +/-2.6')
r('opus55','SWE-bench Multilingual',93.9,'claim','Anthropic','bl_opus','max, system card')
r('opus55','SWE-bench Multimodal',61.4,'claim','Anthropic','bl_opus','max, system card')
r('sol61','DeepSWE v1.1',75.2,'claim','OpenAI','bl_sol','high effort')
r('sol61','OSWorld-2.0 offline (partial)',71.4,'claim','OpenAI','bl_sol','max effort')
r('sol61','Terminal-Bench Science 0.1',57.0,'claim','OpenAI','bl_sol','max effort')
r('sol61','HealthBench Professional',64.2,'claim','OpenAI','oai_sc','length-adjusted')
r('sol61','HealthBench',58.5,'claim','OpenAI','oai_sc','length-adjusted')
r('sol61','HealthBench Hard',36.2,'claim','OpenAI','oai_sc','length-adjusted')
for b,v,n in [('CursorBench 4.0',46.3,'xhigh'),('DeepSWE v1.1',71.0,'high effort (asterisk in xAI table)'),('EEBench',64.0,''),('Terminal-Bench 4.0',37.6,''),('Harvey Legal Agent',19.6,''),('HealthBench Professional',56.7,'')]:
    r('grok47',b,v,'claim','SpaceXAI','xai',n)
for b,v in [('CursorBench 4.0',51.8),('DeepSWE v1.1',70.0),('EEBench',56.4),('Terminal-Bench 4.0',57.9),('Harvey Legal Agent',6.7),('HealthBench Professional',62.1)]:
    r('fable51',b,v,'vendor-table','SpaceXAI','xai','xAI comparison table')
for b,v,n in [('Terminal-Bench 4.0',57.1,'max'),('DeepSWE v1.1',79.0,'max'),('SWE-Marathon',57.5,'xhigh'),('JobBench',75.3,'max'),('HealthBench Professional',62.3,'max'),('Vals Finance Agent v2',59.1,'max'),('Harvey Legal Agent',13.1,'max'),('AutomationBench-AA',45.4,'max, as labeled by Meta/Tokens or Towers'),('OSWorld V2.1 (partial)',78.4,'max; binary 39.4')]:
    r('wfull',b,v,'claim','Meta','tot_muse' if b in('SWE-Marathon','AutomationBench-AA','OSWorld V2.1 (partial)','DeepSWE v1.1','Vals Finance Agent v2') else 'benchlm_muse',n)
# independent
for m,v,s,n in [('argon',53,'aa_argon','high'),('astra',53,'aa_argon','max'),('sol61',52,'aa_argon','max'),('fable51',53,'aa_argon','v4.3 rebase; scored 66 on the older index at launch (aa_fable)'),('grok47',46,'aa_grok','xhigh'),('wfull',56,'aa_muse','max'),('wonder',52,'aa_muse','max'),('spark13',48,'aa_muse','max'),('opus55',58,'aa_kimi','max with fallback; confirmed on AA Kimi K3.1 Pro article (2026-10-23). Previously sourced second-hand from Tokens or Towers.'),('sonnet55',56,'aa_kimi','max with fallback'),('kimi31',55,'aa_kimi','reasoning model, AA launch test'),('sparkopen',39,'aa_beam','value quoted in AA Beam article')]:
    r(m,'AA Intelligence Index v4.3',v,'independent','Artificial Analysis',s,n,unit='index')
for m,v,s,n in [('argon',57,'aa_argon','high'),('astra',59,'aa_argon',''),('opus55',60,'aa_argon','max'),('sonnet55',64,'aa_argon','max'),('wfull',57,'aa_muse','max, AA harness'),('wonder',52,'aa_muse','max'),('grok47',33,'aa_grok','xhigh in Grok Build harness (Coding Agent Index)')]:
    r(m,'Terminal-Bench 4.0',v,'independent','Artificial Analysis',s,n)
r('grok47','DeepSWE v1.1',73,'independent','Artificial Analysis','aa_grok','xhigh in Grok Build harness')
for m,v,s in [('argon',78,'aa_argon'),('sonnet55',71,'aa_argon'),('wfull',71,'aa_muse'),('wonder',68,'aa_muse')]:
    r(m,'AutomationBench-AA',v,'independent','Artificial Analysis',s)
for m,v,s in [('argon',15,'aa_argon'),('astra',51,'aa_argon'),('sol61',54,'aa_argon'),('grok47',29,'aa_grok'),('wfull',23.0,'benchlm_muse')]:
    r(m,'AA-Omniscience hallucination rate (lower better)',v,'independent','Artificial Analysis',s)
for m,v,s in [('wfull',1857,'aa_muse'),('fable51',1853,'aa_fable'),('grok47',1695,'aa_grok')]:
    r(m,'GDPval-AA (Elo)',v,'independent','Artificial Analysis',s,unit='Elo')
for m,v,s in [('wfull',1729,'aa_muse'),('fable51',1694,'aa_fable'),('grok47',1657,'aa_grok'),('argon',1494,'aa_argon')]:
    r(m,'AA-Briefcase (Elo)',v,'independent','Artificial Analysis',s,unit='Elo')
r('fable51',"Humanity's Last Exam",59.1,'independent','Artificial Analysis','aa_fable','max')
r('wfull',"Humanity's Last Exam",53.6,'independent','Artificial Analysis','benchlm_muse','secondary source')
r('fable51','SciCode',62.0,'independent','Artificial Analysis','aa_fable','max')
r('wfull','SciCode',63,'independent','Artificial Analysis','aa_muse','max')
r('wfull','CritPt',33,'independent','Artificial Analysis','aa_muse','max')
r('grok47','SWE-Together',64.7,'independent','SWE-Together evaluators','apidog_grok','pass@1 after sandbox lockdown; 44/218 first-run trials fetched external code')
# ---- added 2026-10-26 ----
# Kimi K3.1 Pro, AA independent (opened page)
r('kimi31','GDPval-AA (Elo)',1846,'independent','Artificial Analysis','aa_kimi',unit='Elo')
r('opus55','GDPval-AA (Elo)',1866,'independent','Artificial Analysis','aa_kimi','max with fallback (quoted in Kimi article)',unit='Elo')
r('kimi31','Terminal-Bench 4.0',67,'independent','Artificial Analysis','aa_kimi','AA harness; AA calls it the highest score of any model on Terminal-Bench 4.0')
r('kimi31','AutomationBench-AA',73,'independent','Artificial Analysis','aa_kimi')
r('kimi31',"Humanity's Last Exam",52,'independent','Artificial Analysis','aa_kimi')
r('kimi31','CritPt',25,'independent','Artificial Analysis','aa_kimi')
r('kimi31','SciCode',61,'independent','Artificial Analysis','aa_kimi')
r('kimi31','AA-Omniscience hallucination rate (lower better)',44,'independent','Artificial Analysis','aa_kimi')
r('kimi31','AA-Omniscience Index',30,'independent','Artificial Analysis','aa_kimi',unit='index')
# Kimi K3.1 Pro vendor claims (Moonshot blog, opened page)
r('kimi31','Terminal-Bench 4.0',65.7,'claim','Moonshot AI','kimi_blog','Claude-Code harness')
r('kimi31','BenchCAD',92.7,'claim','Moonshot AI','kimi_blog','with tools')
r('kimi31','OfficeQA Pro v2',64.4,'claim','Moonshot AI','kimi_blog','Moonshot internal benchmark; Moonshot claims state of the art')
r('opus55','BenchCAD',96.2,'vendor-table','Moonshot AI','kimi_blog','as reported in Moonshot launch post')
r('astra','BenchCAD',95.9,'vendor-table','Moonshot AI','kimi_blog','as reported in Moonshot launch post')
# AA HealthBench leaderboards (length-adjusted, as OpenAI reports)
for m,v,n in [('astra',66.0,'max'),('sol61',65.1,'max'),('sonnet55',63.0,'max with fallback'),('sol6',62.3,'max'),('luna',61.9,'max'),('opus55',59.9,'max with fallback; raw (unadjusted) score 71.4, highest raw score')]:
    r(m,'HealthBench Professional (AA, length-adjusted)',v,'independent','Artificial Analysis','aa_health',n,'Graded by GPT-5.4 (low) per OpenAI implementation.')
r('opus55','HealthBench Professional (AA, raw)',71.4,'independent','Artificial Analysis','aa_health','max with fallback','Raw share of rubric points; not length-adjusted.')
for m,v,n in [('sonnet55',62.1,'max with fallback'),('sol61',58.5,'max'),('luna',54.6,'max')]:
    r(m,'HealthBench (AA, length-adjusted)',v,'independent','Artificial Analysis','aa_health',n,'Graded by GPT-4.1 per OpenAI implementation.')
# AA FrontierCode 1.1 (Cognition benchmark, AA Stirrup harness)
for m,v,n in [('opus55',52,'max with fallback; pass rate 58%'),('sol61',49,'max'),('fable51',49,'max with fallback'),('luna',42,'max')]:
    r(m,'FrontierCode 1.1 Main (AA)',v,'independent','Artificial Analysis','aa_fcode',n,'Mean score over 3 attempts per task, Stirrup harness. Article says Astra (max) is 2 points below GPT-6.1 Sol; not recorded as a separate value.')
r('opus55','FrontierCode 1.1 Main pass rate (AA)',58,'independent','Artificial Analysis','aa_fcode','max with fallback')
# AA Decision Index v1.0 (language-model comparison rows)
r('haiku55','AA Decision Index v1.0',61,'independent','Artificial Analysis','aa_decision','Low effort',unit='index')
r('luna','AA Decision Index v1.0',55,'independent','Artificial Analysis','aa_decision','Low effort',unit='index')
# AA-Robotics v0.1
r('astra','AA-Robotics v0.1',69,'independent','Artificial Analysis','aa_robotics','Codex, high effort','Mean score per task (0 to 100).',unit='score')
r('sol61','AA-Robotics v0.1',65,'independent','Artificial Analysis','aa_robotics','Codex, high effort','Mean score per task (0 to 100).',unit='score')
# AA-3D (Elo, blind human votes)
r('sonnet55','AA-3D (Elo)',1194,'independent','Artificial Analysis','aa_3d','max with fallback','Top four statistically tied per AA.',unit='Elo')
r('spark13','AA-3D (Elo)',1035,'independent','Artificial Analysis','aa_3d','max','7th place.',unit='Elo')
# Arena text leaderboard, overall (Oct 22, 2026 snapshot); +/- is the reported CI
for m,v,ci,n in [('argon',1517,7,'Gemini 4 Argon (High)'),('opus55',1509,7,'Claude Opus 5.5 (High)'),('wonder',1509,8,'Muse Wonder (Max)'),('fable51',1503,6,'Claude Fable 5.1 (Max)'),('spark13',1496,5,'Muse Spark 1.3 (Max)'),('sol61',1480,7,'GPT-6.1 Sol (Max)'),('sonnet55',1478,7,'Claude Sonnet 5.5 (xHigh)'),('astra',1476,6,'GPT-6 Astra (Max)'),('sol6',1459,6,'GPT-6 Sol (Max)'),('luna',1442,4,'GPT-6 Luna (Max)'),('grok47',1441,6,'Grok 4.7 (xHigh)'),('haiku55',1425,8,'Claude Haiku 5.5 (High)')]:
    r(m,'Arena Text (overall)',v,'independent','Arena (LMArena)','arena_text',n,'Score +/- %d as shown on leaderboard dated Oct 22, 2026.'%ci,unit='Elo')
# Muse Spark Open, Meta model page table (opened page; column order checked in page HTML)
for b,v,u in [('JobBench',61.8,'%'),('MCP-Atlas',89.2,'%'),('GDPval-AA v2 (Elo)',1401,'Elo'),('HLE-Diamond (no tools)',26.1,'%'),('SciCode',58.5,'%'),('AA-Omniscience Index',25,'index'),('Terminal-Bench 2.1 (Terminus 2 agent)',76.4,'%'),('DeepSWE 1.1 (best available/self-reported harness)',60,'%'),('ZeroBench',50.0,'%'),('BabyVision',80.2,'%'),('SimpleVQA',73.6,'%')]:
    r('sparkopen',b,v,'claim','Meta','meta_sparkopen','xhigh','Meta table; units not printed on the page, assumed % except Elo and index rows.',unit=u)
PAIRS=[('argon','Terminal-Bench 4.0',57.4,57,'close'),('opus55','Terminal-Bench 4.0',66.4,60,'claim xhigh, Anthropic harness; AA max'),('astra','Terminal-Bench 4.0',58.2,59,'claim value from Google table, "as reported by OpenAI"'),('grok47','Terminal-Bench 4.0',37.6,33,'AA used Grok Build harness'),('wfull','Terminal-Bench 4.0',57.1,57,'close'),('grok47','DeepSWE v1.1',71.0,73,'independent higher than claim'),('argon','AutomationBench vs AA variant',51.3,78,'DIFFERENT variants: Zapier private set vs AutomationBench-AA'),('wfull','AutomationBench vs AA variant',45.4,71,'Labels conflict; likely different variants'),('fable51','DeepSWE v1.1 (Google table vs xAI table)',67.4,70.0,'two rival vendors report different Fable numbers'),('kimi31','Terminal-Bench 4.0',65.7,67,'claim Claude-Code harness; AA harness. Added 2026-10-26'),('sol61','HealthBench Professional',64.2,65.1,'both length-adjusted; OpenAI claim vs AA run. Added 2026-10-26'),('sol61','HealthBench',58.5,58.5,'both length-adjusted; identical. Added 2026-10-26')]
pairs=[dict(model=a,benchmark=b,claim=c,independent=i,gap=round(i-c,1),note=n) for a,b,c,i,n in PAIRS]
data=dict(as_of='2026-10-26',models=[dict(id=a,name=b,maker=c,family=d,release=e,status=f,note=g) for a,b,c,d,e,f,g in M],records=R,pairs=pairs,google_table_benchmarks=GB,sources={k:dict(url=v[0],date=v[1],title=v[2]) for k,v in S.items()},
 not_found=['Any "GPT-6.1 Astra" or other GPT-6.1 variant besides Sol','A Cursor-specific Grok 4.7 model (user said "Cursor with Grok 4.7"); only xAI-reported CursorBench 4.0','SWE-bench Verified, ARC Prize, Epoch, Scale SEAL, GPQA Diamond, AIME, MMMU scores for these models were not located (checked again 2026-10-26; Arena Text scores now included)','GPT-6 Luna release date','Anthropic benchmark claims for Sonnet 5.5 and Haiku 5.5','Arena Text score for Kimi K3.1 Pro and Muse Spark Open (not listed on Oct 22 snapshot)'])
w=csv.writer(open('sources.csv','w',newline=''),lineterminator='\n')
w.writerow(['model','benchmark','value','unit','type','reporter','setting','note','source','date'])
for x in R: w.writerow([x[k] for k in ['model','benchmark','value','unit','type','reporter','setting','note','source','date']])
html=open('template.html').read().replace('/*DATA*/',json.dumps(data)).replace('/*ECHARTS*/',open('echarts.min.js').read() if __import__('os').path.exists('echarts.min.js') else __import__('urllib.request',fromlist=['x']).urlopen('https://cdn.jsdelivr.net/npm/echarts@5.6.0/dist/echarts.min.js').read().decode())
open('index.html','w').write(html)
print(len(R),'records')
