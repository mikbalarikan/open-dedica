"""Compose measure/params.json from the measurement JSONs in measure/figures (scratch copy in figures/src)."""
import json, math, hashlib, datetime, numpy as np, sys
run=sys.argv[1]; F=run+'/measure/figures/'
J=lambda n: json.load(open(F+n))
core,ports,rib,misc,stem=J('core_meas.json'),J('ports_meas.json'),J('rib_meas.json'),J('misc_meas.json'),J('stem_meas.json')
fit=lambda n: J('fit_%s.json'%n)['result']
al=json.load(open(run+'/intake/alignment.json')); noise=al['scan_noise_mm']['value']
def sha(p): return hashlib.sha256(open(p,'rb').read()).hexdigest()
P={}
def add(name,value,unit,measured,rule,source,estimator,unc,evidence,critical=False,**kw):
    P[name]=dict(value=value,unit=unit,measured=measured,rule=rule,source=source,estimator=estimator,uncertainty_mm=unc,evidence=evidence,critical=critical,**kw)
r3=lambda x: round(float(x),3)
N=r3(noise)
TRIG='one caliper reading on this feature triggers a re-run (scan-only run, MEASUREMENTS decision)'
# ---------------- plate
add('flange_floor_z',2.26,'mm',r3(core['floor_z']['p50']),'round-within-noise','scan','p50 z of up-facing faces (n>0.95) on the tray floor, r 8.8-9.2 and ear floors; full-res scan, datum frame',N,'measure/figures/core_meas.json#floor_z',True,rerun_trigger=TRIG,note='flange thickness (back face z=0 is the datum)')
add('rim_top_z',5.63,'mm',r3(core['rim_top_z']['p50']),'round-within-noise','scan','p50 z of up-facing faces r>10, |x|<6, z>4.5',N,'measure/figures/core_meas.json#rim_top_z')
add('plate_R',11.70,'mm',r3(core['plate_central_R']['p50']),'round-within-noise','scan','p50 radius of outward rim-wall faces |x|<5, z 2.6-5.0 (+Y and -Y halves both 11.697)',N,'measure/figures/core_meas.json#plate_central_R',note='fits.py arc fit over theta 60-120 (fit_plate_R.json, r 11.19 with centre offset 0.52) is an ill-conditioned 60 deg arc and is not used')
ex=[core['ear_hole_px']['cx'],core['ear_hole_nx']['cx']]
add('ear_hole_x',[r3(e) for e in ex],'mm',[r3(e) for e in ex],'keep-measured','scan','robust circle fit (soft-L1) to ear-hole wall faces z 0.3-1.9, x of centre, [+X ear, -X ear]',N,'measure/figures/core_meas.json#ear_hole_px/nx',True,frame='datum X (ear axis)',rerun_trigger=TRIG,note='critical: held per hole (|x| 15.447 vs 15.338 differ by 0.109 > noise; not symmetrised, C9). Ear outlines are centred on their own hole.')
P_earx=float(np.mean([abs(e) for e in ex]))
eh=[core['ear_hole_px']['r'],core['ear_hole_nx']['r']]
add('ear_hole_r',round(float(np.mean(eh)),3),'mm',[r3(e) for e in eh],'symmetry','scan','same fit as ear_x, radius',N,'measure/figures/core_meas.json#ear_hole_px/nx',True,scatter_mm=r3(abs(eh[0]-eh[1])),rerun_trigger=TRIG)
xs=np.array([11.5,12.5,13.5,14.5,15.5,16.5]); ys=np.array([core['ear_halfwidth_x%.1f'%x] for x in xs]); b,a=np.polyfit(xs,ys,1)
ang=math.degrees(math.atan(-b)); earx=P_earx; dist=(a+b*earx)/math.sqrt(1+b*b)
tips=[core['ear_tip_x_px']-core['ear_hole_px']['cx'], core['ear_tip_x_nx']+core['ear_hole_nx']['cx']]
add('ear_side_angle_deg',round(ang,2),'deg',round(ang,2),'keep-measured','scan','line fit y=a+bx to outer-wall half-widths at x=11.5..16.5 (both sides pooled, z 2.6-5.0); taper angle = atan(-b)',N,'measure/figures/core_meas.json#ear_halfwidth_*',frame='datum XY, ear axis = +X')
add('ear_end_R',round(dist,3),'mm',f'{min(tips+[dist]):.3f}..{max(tips+[dist]):.3f}','keep-measured','scan','distance from the mean |ear_hole_x| on the axis to the fitted side line (ear end = circle tangent to the sides, centred on the hole); cross-check tip x - ear_x = %.3f (+X, damaged tip) / %.3f (-X)'%tuple(tips),N,'measure/figures/core_meas.json#ear_halfwidth_*, ear_tip_x_*')
bl=[misc['outline_corner_+1-1']['r'],misc['outline_corner_-1+1']['r']]
add('outline_blend_R',round(float(np.mean(bl)),3),'mm',[r3(x) for x in bl],'mean-of-n','scan','robust circle fit to outer-wall faces in the concave disc/ear corners (z 2.6-5.0); 2 of 4 corners fitted (rms 0.023/0.073); the other two fits were rejected (rms 0.44/0.42, not a clean arc)',0.27,'measure/figures/misc_meas.json#outline_corner_*',note='spread 0.54 between the two good corners; mean used')
c=math.cos(math.radians(ang))
rw=[core['plate_central_R']['p50']-core['rim_inner_central_R']['p50']]+[ (core['ear_halfwidth_x%.1f'%x]-core['rim_inner_halfwidth_x%.1f'%x])*c for x in (12.5,14.5,16.5)]
add('rim_wall_t',round(float(np.mean(rw)),3),'mm',[r3(x) for x in rw],'mean-of-n','scan','outer minus inner rim wall (p50 radii at |x|<5; half-widths at x=12.5/14.5/16.5 times cos(taper))',N,'measure/figures/core_meas.json#rim_inner_*')
add('back_edge_R',r3(misc['back_edge_round']['R']),'mm',r3(misc['back_edge_round']['R']),'keep-measured','scan','least-squares quarter-circle fit to the outline inset vs z (z 0.05..1.85, |x|<5) against plate_R; rms %.3f'%misc['back_edge_round']['rms'],0.04,'measure/figures/misc_meas.json#back_edge_round')
# ---------------- collar / tube
f=fit('collar'); add('collar_R',8.06,'mm',r3(f['r']),'round-within-noise','scan','fits.py circle (Kasa) on vertices z 2.7-4.1 r 7.6-8.5; percentile p50 %.3f'%f['check_percentile_r']['p50'],r3(f['residual']['rms']),'measure/figures/fit_collar.json')
add('collar_top_z',4.73,'mm',r3(core['collar_top_z']['p50']),'round-within-noise','scan','p50 z of up-facing faces r 6.5-7.8',N,'measure/figures/core_meas.json#collar_top_z')
f=fit('tube_od'); add('tube_R',r3(f['r']),'mm',r3(f['r']),'keep-measured','scan','fits.py circle on vertices z 5.3-8.6 r 5.8-6.7; percentile p50 %.3f'%f['check_percentile_r']['p50'],r3(f['residual']['rms']),'measure/figures/fit_tube_od.json',True,rerun_trigger=TRIG)
f=fit('tube_bore'); add('tube_bore_r',r3(f['r']),'mm',r3(f['r']),'keep-measured','scan','fits.py circle on vertices z 5.3-8.4 r 4.2-5.0; percentile p50 %.3f'%f['check_percentile_r']['p50'],r3(f['residual']['rms']),'measure/figures/fit_tube_bore.json',True,rerun_trigger=TRIG)
add('tube_top_z',13.68,'mm',r3(core['tube_top_z']['p50']),'round-within-noise','scan','p50 z of up-facing faces r 4.6-6.1 z>12 (p10 %.2f / p90 %.2f: finger tops uneven)'%(core['tube_top_z']['p10'],core['tube_top_z']['p90']),0.15,'measure/figures/core_meas.json#tube_top_z',True,rerun_trigger=TRIG)
add('tube_bore_bottom_z',1.5,'mm',None,'assumed','assumed','bore wall is scanned down to z~1.5-1.9 (coverage loop r 4.19-4.69 z 1.9-6.9); the floor / internal web below is not in the scan',None,'intake/coverage.json; intake/INTAKE_CARD.md E07',note='not observable: bore modelled as a blind cylinder ending at the lowest scanned wall level')
cnt=J('count_tube_slots.json')
add('slot_count',4,'count',int(cnt['count']),'keep-measured','scan','pattern_count.py radius signal, FFT-dominant rotational order 4 at z 10/11.5/13, residual local minimum at every station (CHK-COUNT pass); a mass-signal run gave order 8 (slot-edge harmonic), not used',0.0,'measure/figures/count_tube_slots.json')
sw=core['slot_walls']; th=[]
for s0 in sw:
    off=(s0['pos']+s0['neg'])/2; th.append(round((s0['theta']%360)+math.degrees(off/5.4),2))
add('slot_theta_deg',th,'deg',th,'keep-measured','scan','slot centre = mid-plane of its two side walls (tangential-normal faces z 10-13, r 4.8-6.1), converted to angle at r=5.4; order theta 0/90/180/270',N,'measure/figures/core_meas.json#slot_walls',True,frame='datum frame, theta CCW about +Z from +X (+X = ear axis)',rerun_trigger=TRIG,note='critical drive interface: held per slot, not snapped to 0/90/180/270 (largest offset 0.058 mm > noise)')
sw_all=[s0['pos']-s0['neg'] for s0 in sw]
add('slot_w',[r3(x) for x in sw_all],'mm',[r3(x) for x in sw_all],'keep-measured','scan','wall-to-wall distance of each slot (median |d| of side-wall faces from the slot mid-plane); order as slot_theta_deg',N,'measure/figures/core_meas.json#slot_walls',True,rerun_trigger=TRIG,note='two key sizes: ear-axis slots 3.09/3.04, cross slots 2.72/2.57 (keyed drive); held per slot (C9)')
bx=[core['slot_bottom_z_th0']['p50'],core['slot_bottom_z_th180']['p50']]; by=[core['slot_bottom_z_th90']['p50'],core['slot_bottom_z_th-90']['p50']]
add('slot_bottom_z_x',round(float(np.mean(bx)),3),'mm',[r3(x) for x in bx],'symmetry','scan','p50 z of up-facing faces at the slot bottom (theta 0/180 +/-8 deg)',N,'measure/figures/core_meas.json#slot_bottom_z_*',scatter_mm=r3(abs(bx[0]-bx[1])))
add('slot_bottom_z_y',round(float(np.mean(by)),3),'mm',[r3(x) for x in by],'symmetry','scan','p50 z of up-facing faces at the slot bottom (theta 90/270 +/-8 deg)',N,'measure/figures/core_meas.json#slot_bottom_z_*',scatter_mm=r3(abs(by[0]-by[1])))
# ---------------- stem
st=[s['r'] for s in stem['stations'] if s['z']<=-2.0]
add('stem_R',round(float(np.mean(st)),3),'mm',[r3(x) for x in st],'mean-of-n','scan','Kasa circles on z-sections z -3.5..-2.0 excluding the gusset plane (|sin theta|>0.35); fits.py arc fit fit_stem_top.json (theta 20-160 only, r 6.43) is ill-conditioned and not used',0.045,'measure/figures/stem_meas.json')
zz=np.array([-6.5,-6.0,-5.5,-5.0,-4.5]); rr=np.array([core['stem_r_at_z%.1f'%z] for z in zz]); k,c0=np.polyfit(zz,rr,1)
nk=fit('stem_neck')['r']; zt=(P['stem_R']['value']-c0)/k; zb=(nk-c0)/k
add('stem_cone_half_angle_deg',round(math.degrees(math.atan(k)),2),'deg',round(math.degrees(math.atan(k)),2),'keep-measured','scan','line fit r(z) of outward faces at z -6.5..-4.5 (cone flank), angle from the axis',N,'measure/figures/core_meas.json#stem_r_at_z*',frame='datum, from +Z axis')
add('stem_cone_top_z',round(zt,3),'mm',round(zt,3),'keep-measured','scan','intersection of the cone line with stem_R',0.1,'measure/figures/core_meas.json#stem_r_at_z*')
add('stem_neck_R',r3(nk),'mm',r3(nk),'keep-measured','scan','fits.py circle on vertices z -11.8..-8.3 r 3.7-4.5; percentile p50 %.3f'%fit('stem_neck')['check_percentile_r']['p50'],r3(fit('stem_neck')['residual']['rms']),'measure/figures/fit_stem_neck.json',note='cone bottom (cone line = stem_neck_R) derived in the model: z = %.3f'%zb)
sb=J('stembot_meas.json')['stem_bottom_z']
add('stem_neck_bottom_z',round(sb['p50'],3),'mm',round(sb['p50'],3),'keep-measured','scan','p50 z of the flat underside of the stem cylinder (down-facing faces |y|<1, 1.3<|x|<3.8); the stem cylinder runs straight down through the junction (y=0 section, x=+/-4.0..4.25 from z -12 to -19)',N,'measure/figures/stembot_meas.json',note='ports branch off the sides of this cylinder; the rib hangs below it')
g=[core['gusset_y_nx']['pos']-core['gusset_y_nx']['neg'],2*core['gusset_y_px']['pos']]
add('gusset_t',round(float(np.mean(g)),3),'mm',[r3(x) for x in g],'mean-of-n','scan','-X gusset: distance between its +y/-y face medians; +X gusset: 2 x +y face median (its -y face has no clean faces)',0.06,'measure/figures/core_meas.json#gusset_y_*')
ga=[core['gusset_edge_px']['deg'],core['gusset_edge_nx']['deg']]
add('gusset_angle_deg',round(-float(np.mean(ga)),3),'deg',[r3(-x) for x in ga],'mean-of-n','scan','line fit z(x) of the down-facing gusset edge faces |y|<1.5; angle below horizontal',0.5,'measure/figures/core_meas.json#gusset_edge_*',frame='datum XZ plane')
gx=[core['gusset_edge_px']['x_at_z0'],core['gusset_edge_nx']['x_at_z0']]
add('gusset_x_at_z0',round(float(np.mean(gx)),3),'mm',[r3(x) for x in gx],'mean-of-n','scan','x where the fitted gusset edge line meets z=0 (back face)',0.1,'measure/figures/core_meas.json#gusset_edge_*')
# ---------------- ports [+Y, -Y]
pp=[ports['port_pY'],ports['port_nY']]
L=lambda k: [r3(p[k]) for p in pp]
add('port_elev_deg',L('elev_deg'),'deg',L('elev_deg'),'keep-measured','scan','robust cylinder fit (soft-L1, 3 passes) to outward sleeve faces t 8.5-14; elevation below the XY plane of the fitted axis; order [+Y port, -Y port]',0.3,'measure/figures/ports_meas.json#*.axis_dir',True,frame='datum; port axes in the YZ plane, angle below horizontal',rerun_trigger=TRIG,note='the two ports differ by 0.97 deg (> fit scatter): kept per port, not forced symmetric')
z0=[r3(p['axis_point_at_y0'][2]) for p in pp]
add('port_axis_z0',z0,'mm',z0,'keep-measured','scan','z where each fitted port axis crosses y=0 (x of that point 0.05/0.11: modelled at x=0, see simplifications)',0.1,'measure/figures/ports_meas.json#*.axis_point_at_y0')
nr=L('neck_R_p50'); add('port_neck_R',round(float(np.mean(nr)),3),'mm',nr,'symmetry','scan','median radial distance of outward faces t 3.5-6.2, v<2.5 (away from the stem)',N,'measure/figures/ports_meas.json#*.neck_R_p50',scatter_mm=r3(abs(nr[0]-nr[1])))
ts=L('t_sleeve_start'); add('port_sleeve_t',ts,'mm',ts,'keep-measured','scan','t where the median outward radius (v<0) crosses (neck+sleeve)/2, 0.05 steps',0.1,'measure/figures/ports_meas.json#*.t_sleeve_start')
sr=L('sleeve_R_p50'); add('port_sleeve_R',round(float(np.mean(sr)),3),'mm',sr,'symmetry','scan','median radial distance of outward faces t 8.5-14.5 (cylinder fit R %.3f / %.3f)'%(pp[0]['sleeve_fit']['R'],pp[1]['sleeve_fit']['R']),N,'measure/figures/ports_meas.json#*.sleeve_R_p50',scatter_mm=r3(abs(sr[0]-sr[1])))
for k,nm,est in (('t_block_start_p50','port_block_t0','p50 t of block start faces (N.d<-0.9, r>6.3)'),('t_block_end_p50','port_block_t1','p50 t of block end faces (N.d>0.9, r>6.5)'),('t_end_p50','port_end_t','p50 t of the port mouth face (N.d>0.9, 4.4<r<6.0)')):
    v=L(k); add(nm,v,'mm',v,'keep-measured','scan',est,N,'measure/figures/ports_meas.json#*.'+k,nm=='port_end_t',**({'rerun_trigger':TRIG} if nm=='port_end_t' else {}))
for k,nm,crit in (('block_half_u_p50','port_block_half_u',True),('block_half_v_p50','port_block_half_v',True),('lip_R_p50','port_lip_R',True),('bore_r_p50','port_bore_R',True)):
    v=L(k); add(nm,round(float(np.mean(v)),3),'mm',v,'symmetry','scan',{'port_block_half_u':'median |u| of block side faces normal to X, t 15.6-19.0','port_block_half_v':'median |v| of block faces normal to e2, t 15.6-19.0','port_lip_R':'median radius of outward faces between block end and mouth','port_bore_R':'median radius of inward bore faces t 17.8..mouth-0.3'}[nm],N,'measure/figures/ports_meas.json#*.'+k,crit,scatter_mm=r3(abs(v[0]-v[1])),rerun_trigger=TRIG)
add('port_block_corner_R',0.5,'mm',None,'assumed','assumed','block edge rounding along the port axis: visible as rounded in port sections (portsec_p.png) but not fitted',None,'measure/figures/portsec_p.png',note='assumed; cost <=0.2 mm at 4 block corners per port')
add('port_bore_step_t',r3(ports and misc['port_pY_bore_step_t']['p50']),'mm',r3(misc['port_pY_bore_step_t']['p50']),'keep-measured','scan','p50 t of mouth-facing faces 3.2<r<4.3 in the bore (+Y port only; -Y bore not scanned that deep)',0.2,'measure/figures/misc_meas.json#port_pY_bore_step_t',note='applied to both ports (-Y not observable)')
bp=[x[1] for x in misc['port_pY_bore_profile'] if x[1] is not None and 13.0<=x[0]<=14.5]
add('port_bore2_R',round(float(np.mean(bp)),3),'mm',f'{min(bp):.3f}..{max(bp):.3f}','keep-measured','scan','median inward-face radius per 0.5 mm t station, t 13-14.5 (+Y port)',0.05,'measure/figures/misc_meas.json#port_pY_bore_profile')
add('port_bore2_end_t',12.5,'mm',None,'assumed','assumed','deepest scanned bore wall t~13 (+Y); the passage to the junction is not in the scan',None,'measure/figures/misc_meas.json#port_pY_bore_profile',note='blind end assumed just below the last scanned station')
d0=[pp[i]['slot_wall_t_lo_p50']-pp[i]['t_block_start_p50'] for i in range(2)]; w=[pp[i]['slot_wall_t_hi_p50']-pp[i]['slot_wall_t_lo_p50'] for i in range(2)]
add('port_slot_dt0',round(float(np.mean(d0)),3),'mm',[r3(x) for x in d0],'symmetry','scan','slot near wall (p50 t of +d-facing slot wall faces, |u|>4.8, 1<|v|<5) minus block start',N,'measure/figures/ports_meas.json#*.slot_wall_t_lo_p50',scatter_mm=r3(abs(d0[0]-d0[1])))
add('port_slot_w',round(float(np.mean(w)),3),'mm',[r3(x) for x in w],'symmetry','scan','distance between the two slot wall faces along the port axis',N,'measure/figures/ports_meas.json#*.slot_wall_t_*',True,scatter_mm=r3(abs(w[0]-w[1])),rerun_trigger=TRIG)
vi=L('slot_v_inner_p50'); vo=L('slot_v_outer_p50')
add('port_slot_v_in',round(float(np.mean(vi)),3),'mm',vi,'symmetry','scan','p50 |v| of slot end faces (normal ~e2) below |v|=2.5',N,'measure/figures/ports_meas.json#*.slot_v_inner_p50',scatter_mm=r3(abs(vi[0]-vi[1])),scatter_note='both ports take the same clip; residual +/-0.025 mm')
add('port_slot_v_out',round(float(np.mean(vo)),3),'mm',vo,'symmetry','scan','p50 |v| of slot end faces between |v| 3 and 5',N,'measure/figures/ports_meas.json#*.slot_v_outer_p50',scatter_mm=r3(abs(vo[0]-vo[1])),scatter_note='both ports take the same clip; residual +/-0.019 mm')
rt=[core['rib_x']['pos']-core['rib_x']['neg']]
add('rib_t',r3(rt[0]),'mm',r3(rt[0]),'keep-measured','scan','distance between median x of the rib +x and -x faces (z -23.4..-19.5, |y|<2.5); rib centre x=%.3f'%((core['rib_x']['pos']+core['rib_x']['neg'])/2),0.08,'measure/figures/core_meas.json#rib_x')
add('rib_bottom_z',r3(core['rib_bottom_z']['p50']),'mm',r3(core['rib_bottom_z']['p50']),'keep-measured','scan','p50 z of down-facing faces |x|<1.5 |y|<3 z<-20',N,'measure/figures/core_meas.json#rib_bottom_z')
add('rib_half_len',4.5,'mm',None,'assumed','assumed','rib ends are buried in the port sleeves (flat bottom visible to |y|~3.8 at x=0, sec_x0_zoom.png)',None,'measure/figures/sec_x0_zoom.png',note='any value 3.9..5.5 gives the same outer surface')
doc={'schema':'stl-re/params.json@1','tool':'make_params.py (builder, measure stage)','tool_version':'stl-re-measure-intent@1.0.0',
 'inputs':{'input/scan.stl':sha(run+'/input/scan.stl'),'intake/alignment.json':sha(run+'/intake/alignment.json'),**{f'input/photos/photo_{i}.png':sha(run+f'/input/photos/photo_{i}.png') for i in (1,2,3,4)}},
 'seed':0,'created':datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'),'part':'OD-H22_3-way-valve',
 'frame':'datum frame of intake/alignment.json (frozen): z=0 flange back face, +Z towards the drive tube, Z = valve axis (collar/tube/stem-neck circle centres), +X = flange ear axis (fourier_mass n=2), ports in the YZ plane; theta CCW about +Z from +X. Port-local: t along the port axis from its crossing of y=0, u=+X, v=e2=d x u.',
 'scan_noise_mm':noise,
 'authority':'SCAN-ONLY: no caliper or operator values exist (DECISIONS.md MEASUREMENTS); every scan value is scan-authority, ungated by Tier-1. Photos used for intent only (feature identification, U-clip slots, symmetry).',
 'params':P,'struck':[],
 'simplifications':[
  {'name':'coaxial lower body','modelled_as':'stem neck, ports and rib centred on x=0 and on the Z axis','deviation_cost':'measured lateral offsets 0.05-0.17 mm (stem neck centre (0.124,0.077); port axes x 0.05/0.11 at y=0; rib centre x 0.14); CHK-TILT ~0.5 deg'},
  {'name':'port bore draft','modelled_as':'cylinder port_bore_R from the mouth to port_bore_step_t','deviation_cost':'bore profile 4.14 (t 16.5) .. 4.35 (t 19.5): up to 0.2 mm near the step (misc_meas.json#port_*_bore_profile)'},
  {'name':'ejector-pin circles on port sleeves','modelled_as':'not modelled (plain cylinder)','deviation_cost':'shallow round flats ~0.3 mm deep over t 9-14 on the +/-X sides (port_tr.png, radius dips 5.58 -> ~5.3)'},
  {'name':'+X ear tip damage','modelled_as':'undamaged ear by symmetry','deviation_cost':'tip x 20.70 vs 20.91 (-X): up to ~0.2-0.5 mm local at the torn tip'},
  {'name':'small edge rounds not modelled','modelled_as':'sharp edges at rim top, collar and tube top, stem/plate, cone/neck, neck/sleeve steps','deviation_cost':'<=0.3 mm local (rim top z p10/p90 5.52/5.72; stem r 6.61 at z=0 vs 6.55; cone ends)'},
  {'name':'drive-tube finger tops','modelled_as':'one plane at tube_top_z','deviation_cost':'finger top z p10 13.61 / p90 13.92 / max 13.98: up to 0.3 mm'},
  {'name':'rim wall and tray pocket','modelled_as':'constant-thickness offset of the outline, vertical walls, flat floor','deviation_cost':'rim wall 1.42-1.48 measured; floor z 2.14-2.36 across the tray (ears 2.14/2.28): <=0.12 mm'}],
 'checks':{'CHK-COUNT':{'ran':True,'result':'pass','note':'drive-tube slots: order 4 FFT-dominant and residual local minimum at z 10/11.5/13 (radius signal)'},
  'CHK-ACHIEVABLE':{'ran':False,'result':'pass','note':'not applicable: no caliper or photo readings exist (scan-only run)'},
  'CHK-CLUSTER':{'ran':True,'result':'pass','note':'on-axis material below the junction (r<2.2, z -24..-19) is ONE component, 39 mm2 = the planned bottom rib E14 (cluster_axis_bottom.json); nothing above the tube top (zmax 13.98 = finger tops)'},
  'CHK-FRAME':{'ran':True,'result':'pass','note':'all angles re-measured on the full-res scan in the frozen datum frame; no intake angle copied (the intake clock -84.99 deg is a frame definition, not a part angle)'}},
 'open_questions':['Tilt ~0.5 deg between flange normal and the axis features: moulding warp or design? (modelled perpendicular)','Tube-bore floor, internal web and flow passages are not in the scan (assumed blind bores)','scan_resolution not stated by the user (recorded unknown; evidence suggests full-res)']}
json.dump(doc,open(run+'/measure/params.json','w'),indent=1)
print(len(P),'params')
