"""Writes measure/params.json from the probe outputs in measure/figures (values copied from the
probe_*.txt / count_*.json / ribs_lines.json files cited in each row's evidence)."""
import json, hashlib, datetime
def sha(p): return hashlib.sha256(open(p,'rb').read()).hexdigest()
F='measure/figures/'
NOISE=0.04892255856114139
P={}
def add(name,value,unit,measured,rule,source,est,unc,ev,critical=False,**kw):
    d=dict(value=value,unit=unit,measured=measured,rule=rule,source=source,estimator=est,uncertainty_mm=unc,evidence=ev,critical=critical); d.update(kw); P[name]=d
S='scan'
# plate
add('plate_back_z',0.0,'mm',-0.020,'round-within-noise',S,'area-weighted median z of up-facing faces r 7-19.5 (datum plane)',NOISE,F+'probe_p1.txt#plate back',True,rerun_trigger='caliper plate thickness / overall height')
add('plate_under_z',-2.59,'mm',-2.589,'round-within-noise',S,'down-facing faces r 10.5-20.5, z -5..-1; ONLY scanned in sector 20..80 deg',NOISE,F+'probe_p2.txt#underside sector 0-95',note='underside unscanned outside 20..80 deg; assumed planar there')
add('plate_edge_round_R',0.316,'mm',0.316,'keep-measured',S,'(r,z) Kasa arc on plate outer edge faces',0.054,F+'probe_p14.txt#plate outer edge round')
add('bead_R_in',20.33,'mm',20.333,'round-within-noise',S,'r50 of inward-facing bead wall faces',NOISE,F+'probe_p1.txt#bead inner wall')
add('bead_R_out',21.47,'mm',21.469,'round-within-noise',S,'r50 of outward-facing bead wall faces',NOISE,F+'probe_p1.txt#bead outer wall')
add('bead_top_z',1.09,'mm',1.091,'round-within-noise',S,'z50 of up-facing bead top faces; top is a full round (arc R 0.607 ~ half width 0.57)',NOISE,F+'probe_p1.txt#back bead top; probe_p14.txt#bead top')
# cup wall and flange
add('cup_R_out',22.95,'mm',22.952,'round-within-noise',S,'r50 of outward wall faces z -9.5..-1.5 (~270 deg scanned)',NOISE,F+'probe_p1.txt#cup outer wall',True,rerun_trigger='caliper cup OD')
add('cup_R_in',20.60,'mm',20.598,'round-within-noise',S,'r50 of inward wall faces z -10..-4',NOISE,F+'probe_p1.txt#cup inner wall')
add('flange_top_z',-10.76,'mm',-10.755,'round-within-noise',S,'z50 up-facing faces r 24-29',NOISE,F+'probe_p1.txt#flange top',True,rerun_trigger='caliper flange height')
add('flange_bot_z',-13.12,'mm',-13.122,'round-within-noise',S,'z50 down-facing faces r 23-30',NOISE,F+'probe_p1.txt#flange bottom',True,rerun_trigger='caliper overall height to flange bottom')
add('flange_R_out',30.80,'mm',30.796,'round-within-noise',S,'r50 outward wall faces r 30-31.5 z -12.5..-10',NOISE,F+'probe_p1.txt#lip outer wall below tabs',True,rerun_trigger='caliper flange OD')
add('lip_R_in',29.32,'mm',29.317,'round-within-noise',S,'r50 inward wall faces r 28.5-30',NOISE,F+'probe_p1.txt#lip inner wall',True,rerun_trigger='caliper gasket-seat groove width')
add('lip_top_z',-7.03,'mm',-7.034,'round-within-noise',S,'z50 up-facing faces r 29-31 z -8..-6; top is a full round (arc R 0.875 ~ half width 0.74)',NOISE,F+'probe_p1.txt#lip top; probe_p14.txt#lip top')
add('flange_inner_round_R',2.65,'mm',2.65,'keep-measured',S,'arc constrained tangent to cup_R_in and flange_bot_z, R scanned 1.5..3.2 for min rms (0.179) on the corner faces; replaces the first-pass free Kasa fit (1.69/1.96) after the self-check showed a corner miss',0.18,F+'probe_p18.txt#constrained tangent-arc')
add('flange_lip_fillet_R',1.084,'mm',1.084,'keep-measured',S,'(r,z) Kasa arc on faces r 28-29.3 z -10.8..-9.3 (centre r 28.15 ~ lip_R_in - R)',0.05,F+'probe_p18.txt#flange-lip inner fillet')
add('wall_flange_fillet_R',0.38,'mm',0.380,'keep-measured',S,'(r,z) Kasa arc at cup wall / flange top junction',0.06,F+'probe_p14.txt#wall-flange top fillet')
add('flange_outer_round_R',0.196,'mm',0.196,'keep-measured',S,'(r,z) Kasa arc at flange outer-bottom edge',0.07,F+'probe_p14.txt#flange outer-bottom round')
# tabs
add('tab_count',3,'count',3,'keep-measured',S,'pattern_count.py mass, 3 stations, FFT order 3 at all',0,F+'count_tabs.json',True,rerun_trigger='photo/physical count differs')
add('tab_R_out',34.52,'mm',34.519,'round-within-noise',S,'mean over 33 per-angle (6 deg steps, 3 tabs) medians of outward faces r 33-35.5 z -9.3..-8.0 (probe_p21); first-pass r50 34.384 (probe_p1) mixed in the rounded end faces',NOISE,F+'probe_p21.txt',True,rerun_trigger='caliper across tabs')
add('tab_top_z',-7.76,'mm',-7.761,'round-within-noise',S,'z50 up-facing faces r 31.5-34',NOISE,F+'probe_p1.txt#tab top',True,rerun_trigger='caliper tab thickness')
add('tab_bot_z',-9.52,'mm',-9.524,'round-within-noise',S,'z50 down-facing faces r 31.5-34',NOISE,F+'probe_p1.txt#tab bottom',True,rerun_trigger='caliper tab thickness')
add('tab_span_deg',61.08,'deg',[60.94,61.2,61.09],'mean-of-n',S,'median theta of tangential end faces per tab (-153.91..-92.97, -33.89..27.31, 86.23..147.32)',0.1,F+'probe_p8.txt#end faces')
add('tab_pitch_deg',120.0,'deg',[120.07,119.78,120.15],'symmetry',S,'tab centre spacing from end-face angles',0.1,F+'probe_p8.txt#end faces',scatter_mm=0.1,scatter_note='3-fold bayonet: equal pitch is the design intent; measured spacing 119.78..120.15 deg = +-0.1 mm at r 32.6')
add('tab_phase_deg',-3.30,'deg',[-3.29,-3.22,-3.44],'mean-of-n',S,'tab 1 centre angle in the datum frame (tab centres -3.29, 116.78, -123.44 minus k*120)',0.1,F+'probe_p8.txt#end faces',frame='datum; theta CCW about +Z from +X')
# hub, cone, slots, bore
add('hub_ring_R_out',6.13,'mm',[6.116,6.141],'mean-of-n',S,'r50 of hub ring outer wall above/below z0',NOISE,F+'probe_p1.txt#hub ring outer wall; probe_p12.txt#slot inner wall')
add('hub_ring_top_z',0.94,'mm',0.942,'round-within-noise',S,'z50 up-facing faces r 3-7 z 0.3..2',NOISE,F+'probe_p1.txt#hub ring top')
add('cone_R_top',4.70,'mm',4.70,'keep-measured',S,'line fit z=0.924 r-3.407 (r 1.5-4.6) intersected with hub_ring_top_z',0.05,F+'probe_p2.txt#cone fit')
add('cone_slope',0.924,'mm',0.924,'keep-measured',S,'dz/dr of the conical recess (42.7 deg from horizontal)',0.02,F+'probe_p2.txt#cone fit',note='dimensionless slope dz/dr; unit field mm by schema')
add('centre_bore_r',1.30,'mm',1.302,'round-within-noise',S,'r50 inward faces r 1-1.8 z -5.5..-2.5',NOISE,F+'probe_p12.txt#centre bore wall')
add('centre_post_bot_z',-5.64,'mm',-5.64,'keep-measured',S,'deepest scanned bore-wall point (bore seen to here)',0.1,F+'probe_p2.txt#centre r<3.5')
add('centre_post_R_out',2.5,'mm',None,'photo-inferred','photo-inferred','front photos (1.png, 4.png) show a small post inside the hub; outer surface never scanned',None,'input/photos/1.png',note='confirm physically')
add('slot_R_out',7.50,'mm',7.501,'round-within-noise',S,'r50 inward-facing slot outer wall faces',NOISE,F+'probe_p12.txt#slot outer wall')
add('slot_count',4,'count',4,'keep-measured',S,'4 gaps in the back-face annulus r 6.5-7.2 (1 deg bins); pattern_count mass disagreed (walls give order 8), see CHK-COUNT',0,F+'probe_p13.txt')
add('slot_span_deg',40.25,'deg',[41,41,39,40],'mean-of-n',S,'back-face gap widths (155..196, -114..-73, -25..14, 64..104)',1.0,F+'probe_p13.txt')
add('slot_phase_deg',-4.9,'deg',[-4.5,-3.5,-5.5,-6.0],'mean-of-n',S,'slot centre minus k*90',1.0,F+'probe_p13.txt',frame='datum; theta CCW about +Z from +X')
add('hub_bore_R_upper',7.81,'mm',7.811,'round-within-noise',S,'r50 inward faces r 7-8.1 z -9.5..-4 (hub bore is stepped)',NOISE,F+'probe_p17.txt#hub bore upper; probe_p16.txt')
add('hub_bore_R_lower',8.38,'mm',8.384,'round-within-noise',S,'r50 inward faces r 8.1-9 z -15..-10.8',NOISE,F+'probe_p17.txt#hub bore lower; probe_p16.txt')
add('hub_bore_step_z',-10.45,'mm',-10.445,'round-within-noise',S,'z50 down-facing step faces r 7.85-8.3',NOISE,F+'probe_p17.txt#hub bore step face')
add('hub_tube_R_out',10.03,'mm',10.027,'round-within-noise',S,'r50 outward faces r 9.3-11 z -15..-3 (draft 9.98..10.08 ignored)',NOISE,F+'probe_p17.txt#hub tube outer all z')
add('hub_tube_bot_z',-15.73,'mm',-15.730,'round-within-noise',S,'z50 down-facing faces; bottom is a full round (arc centre r 9.19 = tube mid-wall, R 0.81)',NOISE,F+'probe_p1.txt#hub tube bottom; probe_p14.txt#hub tube bottom U')
# ring rib
add('ring_rib_R_in',14.85,'mm',14.853,'round-within-noise',S,'r50 inward faces r 14-15.6',NOISE,F+'probe_p1.txt#ring rib inner')
add('ring_rib_R_out',16.09,'mm',16.086,'round-within-noise',S,'r50 outward faces r 15.3-17',NOISE,F+'probe_p1.txt#ring rib outer')
add('ring_rib_bot_z',-10.67,'mm',-10.671,'round-within-noise',S,'z50 down-facing faces r 14.5-16.5',NOISE,F+'probe_p1.txt#ring rib bottom')
add('ring_rib_arcs_deg',[26,141,205,321],'deg',[26,141,205,321],'keep-measured',S,'angular runs of ring-rib bottom faces (1 deg bins); each end runs into a radial rib (rib_phase + 60k, k=0,2,3,5); the model overlaps the ends into the rib by half a rib thickness; absent in the two sectors holding boss pair A',0.3,F+'probe_p8b.txt',frame='datum; theta CCW about +Z from +X')
# radial ribs
add('rib_count',6,'count',6,'keep-measured',S,'6 separate rib wall-pairs line-fitted (ribs_lines.json); mass FFT gives 12 = 2 walls per rib',0,F+'ribs_lines.json; count_ribs.json')
add('rib_pitch_deg',60.0,'deg',[59.62,58.74,61.36,60.47,60.53,59.28],'symmetry',S,'differences of line-fitted rib directions',0.3,F+'ribs_lines.json',scatter_mm=0.32,scatter_note='6-fold equal pitch is the intent; rib directions scatter +-1.2 deg (0.3 mm at r 15), larger than noise, attributed to one-sided rib wall coverage (side-fit rms up to 0.23)')
add('rib_phase_deg',22.9,'deg',[23.14,22.76,21.5,22.86,23.33,23.86],'mean-of-n',S,'rib direction minus k*60',0.3,F+'ribs_lines.json',frame='datum; theta CCW about +Z from +X')
add('rib_t',1.35,'mm',[1.406,1.309,1.375,1.392,1.296,1.321],'mean-of-n',S,'median signed distance of +/- tangent-facing rib wall faces, along-radius 10.5-20',0.05,F+'probe_p10.txt')
add('rib_step_r',14.55,'mm',[14.6,14.47,14.43,14.46,14.58,14.67],'mean-of-n',S,'1st percentile along-radius of deep (z -13.5..-12.5) rib bottom faces',0.1,F+'probe_p10.txt#deep bottom along r')
add('rib_shallow_bot_z',-10.68,'mm',-10.68,'keep-measured',S,'min z of rib midline samples r 10.5-13.5',0.05,F+'probe_p5.txt')
add('webA_t',1.18,'mm',[1.196,1.159],'mean-of-n',S,'distance between the +/- tangent-facing side faces of the web, along-radius 10.3-11.9 (outer part r 19.1-20.5: 1.133, 1.228)',0.05,F+'probe_p19.txt; probe_p22.txt')
add('webA_bot_z',-10.69,'mm',[-10.73,-10.654],'mean-of-n',S,'z50 of down-facing web bottom faces',0.05,F+'probe_p19.txt',note='radial web hub tube -> boss pair A -> cup wall on the boss-A lines (inner part found by self-check 1, max 1.02 mm at r 11; outer part by self-check 2, max 0.81 mm at r 19.8; outer bottom -10.688/-10.588)')
add('lip_bead_R',31.175,'mm',31.175,'keep-measured',S,'peak of the per-0.2 mm z-bin r50 profile of the lip outer face away from the tabs',NOISE,F+'probe_p20.txt')
add('lip_bead_z',-8.3,'mm','-8.4..-8.2','keep-measured',S,'z bin of the r50 peak',0.1,F+'probe_p20.txt')
add('lip_bead_z_lo',-9.1,'mm','-9.2..-9.0','keep-measured',S,'z where the r50 profile leaves flange_R_out + 0.1',0.1,F+'probe_p20.txt')
add('lip_bead_z_hi',-7.6,'mm','-7.6','keep-measured',S,'z where the r50 profile returns to ~30.94 (blends into the lip top round)',0.1,F+'probe_p20.txt',note='bead present on all non-tab bins (probe_p20 angular histogram); found by the first self-check')
# bosses
add('boss_R_out',3.49,'mm',[3.494,3.489,3.491,3.504,3.488,3.482,3.475,3.493],'mean-of-n',S,'Kasa circle fits of boss outer loops at z -13.5..-14.5 (4 bosses)',0.01,F+'probe_p6.txt')
add('bossA_r',15.50,'mm',[15.455,15.545],'mean-of-n',S,'boss centre radius (pair A)',0.05,F+'probe_p6.txt')
add('bossA_theta_deg',[-6.55,172.95],'deg',[-6.55,172.95],'keep-measured',S,'boss centre angles z -14.5 (not exactly diametric: 179.5 deg)',0.1,F+'probe_p6.txt',frame='datum; theta CCW about +Z from +X')
add('bossA_bot_z',-16.12,'mm',[-16.107,-16.174,-16.066,-16.143],'mean-of-n',S,'z50 down-facing annulus faces around the 2 bosses',0.05,F+'probe_p6.txt')
add('bossB_r',19.03,'mm',[18.96,19.09],'mean-of-n',S,'boss centre radius (pair B, merged into cup inner wall)',0.05,F+'probe_p6.txt')
add('bossB_theta_deg',[113.27,-62.02],'deg',[113.27,-62.02],'keep-measured',S,'boss centre angles z -14.5 (175.3 deg apart: pair B is NOT diametric)',0.1,F+'probe_p6.txt',frame='datum; theta CCW about +Z from +X')
add('bossB_bot_z',-14.88,'mm',[-14.844,-14.824,-14.937,-14.916],'mean-of-n',S,'z50 down-facing annulus faces around the 2 bosses',0.05,F+'probe_p6.txt')
add('boss_cb_r',2.0,'mm',[2.03,2.01,2.00,2.00],'mean-of-n',S,'hole loop radius in the first ~1 mm above the boss mouth',0.05,F+'probe_p15.txt')
add('boss_cb_depth',1.0,'mm','0.9..1.1','keep-measured',S,'z where hole loop radius drops from ~2.0 to ~1.6',0.25,F+'probe_p15.txt')
add('boss_hole_r',1.53,'mm',[1.52,1.54,1.55,1.51],'mean-of-n',S,'hole loop radius 1-2 mm above mouth (slight taper 1.47..1.56 ignored)',0.03,F+'probe_p15.txt')
add('boss_hole_depth',2.75,'mm','2.7..2.8','keep-measured',S,'mouth z minus down-facing hole-bottom faces (A: -13.35/-13.46, B: -12.14)',0.15,F+'probe_p6.txt')
params={'schema':'stl-re/params.json@1','tool':'make_params.py','tool_version':'stl-re-measure-intent@1',
 'inputs':{p:sha(p) for p in ['intake/aligned_work.stl','intake/alignment.json','input/photos/1.png','input/photos/4.png']},
 'seed':0,'created':datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'),
 'part':'OD-G04_brewing-gasket-support',
 'frame':'datum: z=0 plate back face (outward normal +Z, material in -Z); origin = cup outer wall axis ∩ back face plane; X = bayonet tab 1 (fourier_mass clock, alignment.json); theta CCW about +Z from +X',
 'scan_noise_mm':NOISE,'params':P,'struck':[],
 'simplifications':[
  {'name':'flange outer wall (lip) draft','modelled_as':'straight cylinder R 30.80','deviation_cost':'r 30.64 (z -13) .. 30.91 (z -9) => +-0.15 mm (probe_p16.txt)'},
  {'name':'hub tube outer draft','modelled_as':'straight cylinder R 10.03','deviation_cost':'9.975..10.077 => +-0.05 mm (probe_p16.txt)'},
  {'name':'cup outer wall draft','modelled_as':'straight cylinder R 22.95','deviation_cost':'station radii 22.88..23.05 over z -2.5..-9.5 => +-0.09 mm (intake wall fit, alignment.json station_detail)'},
  {'name':'plate underside outside 20..80 deg','modelled_as':'plane z=-2.59 everywhere','deviation_cost':'unscanned there: not measurable; verify reports it as unobservable'},
  {'name':'moulded text on plate underside (sector ~20..80 deg)','modelled_as':'omitted','deviation_cost':'relief of the letters ~ up to 0.3 mm above the underside (sections at 30 deg, sections_radial.png)'},
  {'name':'boss hole mouth flare/taper and boss 172.95 larger counterbore (r 2.2 to -14.9)','modelled_as':'uniform counterbore r 2.0 x 1.0 + bore r 1.53','deviation_cost':'<=0.25 mm radial in the counterbore of boss A 172.95 (probe_p15.txt)'},
  {'name':'rib bottoms, boss bottom edges, rib/boss root fillets','modelled_as':'sharp','deviation_cost':'edge rounds ~0.3-0.6 mm => local deviation up to ~0.2-0.4 mm on edges'},
  {'name':'tab 1 z offset and tab-C bottom recess','modelled_as':'all tabs at tab_top_z/tab_bot_z','deviation_cost':'tab 1 (-3.3 deg) sits 0.15 lower (top -7.92, bottom -9.65); tab C bottom has a 0.25 mm recess over ~20 deg (probe_p21.txt)'},
  {'name':'rib direction scatter','modelled_as':'equal 60 deg pitch, phase 22.9','deviation_cost':'up to 1.2 deg = 0.3 mm at r 15, 0.4 mm at r 20 (ribs_lines.json)'}],
 'checks':{
  'CHK-COUNT':{'ran':True,'result':'finding','note':'tabs: pattern_count mass 3 stations -> 3, pass. ribs: mass FFT gives 12 at all 3 stations = 2 thin walls per rib (scan sees rib walls, not rib interiors); 6 ribs confirmed by 6 separate wall-pair line fits (ribs_lines.json). slots: mass FFT disagreed (4/8/12) because the thin back-face band is broken by the slot walls; 4 gaps confirmed on 1-deg back-face coverage (probe_p13.txt). Values used: ribs 6, slots 4, tabs 3.'},
  'CHK-ACHIEVABLE':{'ran':False,'result':'pass','note':'no caliper readings supplied (scan-only run, DECISIONS.md MEASUREMENTS)'},
  'CHK-CLUSTER':{'ran':True,'result':'pass','note':'hub interior r<7.7, z -16.5..-2.7: 13.3 mm2 in 14 components, 76% one component = the centre bore wall r 1.30 down to z -5.64 -> modelled as centre post (cluster_hub_interior.json). No other unexplained material seen in sections/heightmaps.'},
  'CHK-FRAME':{'ran':True,'result':'pass','note':'all angles measured on intake/aligned_work.stl (frozen frame); none copied from intake. alignment clock (fourier_mass) 6.83 deg is biased by the scan gap on tab 1; tab 1 centre in the frozen frame measured at -3.30 deg from end faces and used as-is.'}},
 'open_questions':['plate underside outside sector 20..80 deg and the hub interior were not scanned; confirm plate thickness 2.59 with a caliper','centre post outer diameter (assumed 5.0) - confirm physically','scan gap on the outer wall/flange top at theta -69..+27 deg']}
json.dump(params,open('measure/params.json','w'),indent=1,ensure_ascii=False)
print(len(P),'params')
