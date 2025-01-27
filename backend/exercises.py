from pose_detection import *
vis_thresh = 0.7
def count_bicep_curl(cur_session,detector,lmList):
    if lmList['right_shoulder'][2] > vis_thresh and lmList['right_elbow'][2] > vis_thresh and lmList['right_wrist'][2] > vis_thresh:
        relbow_angle = detector.calc_angle(lmList['right_shoulder'], lmList['right_elbow'], lmList['right_wrist'])

        if cur_session['up'] and relbow_angle < 30:
            cur_session['reps'] += 0.5
            cur_session['up'] = False
        elif not cur_session['up'] and relbow_angle > 150: 
            cur_session['reps'] += 0.5
            cur_session['up'] = True;

def count_situp(cur_session,detector,lmList):
    if ((lmList['right_shoulder'][2] > vis_thresh and lmList['right_hip'][2] > vis_thresh and lmList['right_ankle'][2] > vis_thresh) or
    (lmList['left_shoulder'][2] > vis_thresh and lmList['left_hip'][2] > vis_thresh and lmList['left_ankle'][2] > vis_thresh)):
        rhip_angle = detector.calc_angle(lmList['right_shoulder'], lmList['right_hip'], lmList['right_ankle'])
        lhip_angle = detector.calc_angle(lmList['left_shoulder'], lmList['left_hip'], lmList['left_ankle'])

        if cur_session['up'] and (rhip_angle < 90 or lhip_angle < 90):
            cur_session['reps'] += 0.5
            cur_session['up'] = False
        elif not cur_session['up'] and (rhip_angle > 150 or lhip_angle > 150): 
            cur_session['reps'] += 0.5
            cur_session['up'] = True;

def count_squat(cur_session,detector,lmList):
    if ((lmList['right_hip'][2] > vis_thresh and lmList['right_knee'][2] > vis_thresh and lmList['right_ankle'][2] > vis_thresh) or
    (lmList['left_hip'][2] > vis_thresh and lmList['left_knee'][2] > vis_thresh and lmList['left_ankle'][2] > vis_thresh)):
        rknee_angle = detector.calc_angle(lmList['right_hip'], lmList['right_knee'], lmList['right_ankle'])
        lknee_angle = detector.calc_angle(lmList['left_hip'], lmList['left_knee'], lmList['left_ankle'])

        if cur_session['up'] and (rknee_angle < 85 or lknee_angle < 85):
            cur_session['reps'] += 0.5
            cur_session['up'] = False
        elif not cur_session['up'] and (rknee_angle > 160 or lknee_angle > 160): 
            cur_session['reps'] += 0.5
            cur_session['up'] = True;