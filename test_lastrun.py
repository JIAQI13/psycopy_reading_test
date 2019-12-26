#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on 十二月 25, 2019, at 17:24
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'test'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\15725\\Desktop\\psy\\test_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
ins = visual.TextStim(win=win, name='ins',
    text='In this lab, you will see a block of text come up on the screen. You are asked to read out aloud the text and press Enter when you are done. After each text, you will be asked one question about the text that you just read. You will be given 4 choices for each question, please select the right answer by pressing the appropriate number key. You will get a break after 10 texts, you can press the Enter button if you want to skip that break. \n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ins_key = keyboard.Keyboard()

# Initialize components for Routine "trial_readtime"
trial_readtimeClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
test_key = keyboard.Keyboard()
total_acc = 0
key_press = 0
timer = core.Clock()
begin = timer.getTime()
end = 0

# Initialize components for Routine "trial_choose"
trial_chooseClock = core.Clock()
text_choose = visual.TextStim(win=win, name='text_choose',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_choose = keyboard.Keyboard()

# Initialize components for Routine "session_begin"
session_beginClock = core.Clock()
text_begin = visual.TextStim(win=win, name='text_begin',
    text='session begins\npress return',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "trial_readtime"
trial_readtimeClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
test_key = keyboard.Keyboard()
total_acc = 0
key_press = 0
timer = core.Clock()
begin = timer.getTime()
end = 0

# Initialize components for Routine "trial_choose"
trial_chooseClock = core.Clock()
text_choose = visual.TextStim(win=win, name='text_choose',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_choose = keyboard.Keyboard()

# Initialize components for Routine "end"
endClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='end',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
# update component parameters for each repeat
ins_key.keys = []
ins_key.rt = []
# keep track of which components have finished
instructionsComponents = [ins, ins_key]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ins* updates
    if ins.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ins.frameNStart = frameN  # exact frame index
        ins.tStart = t  # local t and not account for scr refresh
        ins.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ins, 'tStartRefresh')  # time at next scr refresh
        ins.setAutoDraw(True)
    
    # *ins_key* updates
    waitOnFlip = False
    if ins_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ins_key.frameNStart = frameN  # exact frame index
        ins_key.tStart = t  # local t and not account for scr refresh
        ins_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ins_key, 'tStartRefresh')  # time at next scr refresh
        ins_key.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(ins_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if ins_key.status == STARTED and not waitOnFlip:
        theseKeys = ins_key.getKeys(keyList=['return'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ins.started', ins.tStartRefresh)
thisExp.addData('ins.stopped', ins.tStopRefresh)
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('sample_test.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial_readtime"-------
    # update component parameters for each repeat
    text.setText(sentence

)
    test_key.keys = []
    test_key.rt = []
    # keep track of which components have finished
    trial_readtimeComponents = [text, test_key]
    for thisComponent in trial_readtimeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_readtimeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "trial_readtime"-------
    while continueRoutine:
        # get current time
        t = trial_readtimeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_readtimeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *test_key* updates
        waitOnFlip = False
        if test_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test_key.frameNStart = frameN  # exact frame index
            test_key.tStart = t  # local t and not account for scr refresh
            test_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test_key, 'tStartRefresh')  # time at next scr refresh
            test_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(test_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(test_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if test_key.status == STARTED and not waitOnFlip:
            theseKeys = test_key.getKeys(keyList=['return'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                test_key.keys = theseKeys.name  # just the last key pressed
                test_key.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_readtimeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_readtime"-------
    for thisComponent in trial_readtimeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('text.started', text.tStartRefresh)
    trials_2.addData('text.stopped', text.tStopRefresh)
    # check responses
    if test_key.keys in ['', [], None]:  # No response was made
        test_key.keys = None
    trials_2.addData('test_key.keys',test_key.keys)
    if test_key.keys != None:  # we had a response
        trials_2.addData('test_key.rt', test_key.rt)
    trials_2.addData('test_key.started', test_key.tStartRefresh)
    trials_2.addData('test_key.stopped', test_key.tStopRefresh)
    if(test_key.corr == 1):
        total_acc = total_acc + 1
    key_press = key_press + 4
    if(key_press == 4):
        text.finished = True
    # the Routine "trial_readtime" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trial_choose"-------
    # update component parameters for each repeat
    key_choose.keys = []
    key_choose.rt = []
    # keep track of which components have finished
    trial_chooseComponents = [text_choose, key_choose]
    for thisComponent in trial_chooseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_chooseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "trial_choose"-------
    while continueRoutine:
        # get current time
        t = trial_chooseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_chooseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_choose* updates
        if text_choose.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_choose.frameNStart = frameN  # exact frame index
            text_choose.tStart = t  # local t and not account for scr refresh
            text_choose.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_choose, 'tStartRefresh')  # time at next scr refresh
            text_choose.setAutoDraw(True)
        if text_choose.status == STARTED:  # only update if drawing
            text_choose.setText(sentence+ '\n 1' + choose_A + '\n 2 '+ choose_B + '\n 3 ' + choose_C + '\n 4 ' + choose_D, log=False)
        
        # *key_choose* updates
        waitOnFlip = False
        if key_choose.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_choose.frameNStart = frameN  # exact frame index
            key_choose.tStart = t  # local t and not account for scr refresh
            key_choose.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_choose, 'tStartRefresh')  # time at next scr refresh
            key_choose.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_choose.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_choose.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_choose.status == STARTED and not waitOnFlip:
            theseKeys = key_choose.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_choose.keys = theseKeys.name  # just the last key pressed
                key_choose.rt = theseKeys.rt
                # was this 'correct'?
                if (key_choose.keys == str(correctAns)) or (key_choose.keys == correctAns):
                    key_choose.corr = 1
                else:
                    key_choose.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_chooseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_choose"-------
    for thisComponent in trial_chooseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('text_choose.started', text_choose.tStartRefresh)
    trials_2.addData('text_choose.stopped', text_choose.tStopRefresh)
    # check responses
    if key_choose.keys in ['', [], None]:  # No response was made
        key_choose.keys = None
        # was no response the correct answer?!
        if str(correctAns).lower() == 'none':
           key_choose.corr = 1;  # correct non-response
        else:
           key_choose.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('key_choose.keys',key_choose.keys)
    trials_2.addData('key_choose.corr', key_choose.corr)
    if key_choose.keys != None:  # we had a response
        trials_2.addData('key_choose.rt', key_choose.rt)
    trials_2.addData('key_choose.started', key_choose.tStartRefresh)
    trials_2.addData('key_choose.stopped', key_choose.tStopRefresh)
    # the Routine "trial_choose" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


# ------Prepare to start Routine "session_begin"-------
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
# keep track of which components have finished
session_beginComponents = [text_begin, key_resp]
for thisComponent in session_beginComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
session_beginClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "session_begin"-------
while continueRoutine:
    # get current time
    t = session_beginClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=session_beginClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_begin* updates
    if text_begin.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_begin.frameNStart = frameN  # exact frame index
        text_begin.tStart = t  # local t and not account for scr refresh
        text_begin.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_begin, 'tStartRefresh')  # time at next scr refresh
        text_begin.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['return'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp.keys = theseKeys.name  # just the last key pressed
            key_resp.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in session_beginComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "session_begin"-------
for thisComponent in session_beginComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_begin.started', text_begin.tStartRefresh)
thisExp.addData('text_begin.stopped', text_begin.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "session_begin" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('test.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial_readtime"-------
    # update component parameters for each repeat
    text.setText(sentence

)
    test_key.keys = []
    test_key.rt = []
    # keep track of which components have finished
    trial_readtimeComponents = [text, test_key]
    for thisComponent in trial_readtimeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_readtimeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "trial_readtime"-------
    while continueRoutine:
        # get current time
        t = trial_readtimeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_readtimeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *test_key* updates
        waitOnFlip = False
        if test_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test_key.frameNStart = frameN  # exact frame index
            test_key.tStart = t  # local t and not account for scr refresh
            test_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test_key, 'tStartRefresh')  # time at next scr refresh
            test_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(test_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(test_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if test_key.status == STARTED and not waitOnFlip:
            theseKeys = test_key.getKeys(keyList=['return'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                test_key.keys = theseKeys.name  # just the last key pressed
                test_key.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_readtimeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_readtime"-------
    for thisComponent in trial_readtimeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
    # check responses
    if test_key.keys in ['', [], None]:  # No response was made
        test_key.keys = None
    trials.addData('test_key.keys',test_key.keys)
    if test_key.keys != None:  # we had a response
        trials.addData('test_key.rt', test_key.rt)
    trials.addData('test_key.started', test_key.tStartRefresh)
    trials.addData('test_key.stopped', test_key.tStopRefresh)
    if(test_key.corr == 1):
        total_acc = total_acc + 1
    key_press = key_press + 4
    if(key_press == 4):
        text.finished = True
    # the Routine "trial_readtime" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trial_choose"-------
    # update component parameters for each repeat
    key_choose.keys = []
    key_choose.rt = []
    # keep track of which components have finished
    trial_chooseComponents = [text_choose, key_choose]
    for thisComponent in trial_chooseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_chooseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "trial_choose"-------
    while continueRoutine:
        # get current time
        t = trial_chooseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_chooseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_choose* updates
        if text_choose.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_choose.frameNStart = frameN  # exact frame index
            text_choose.tStart = t  # local t and not account for scr refresh
            text_choose.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_choose, 'tStartRefresh')  # time at next scr refresh
            text_choose.setAutoDraw(True)
        if text_choose.status == STARTED:  # only update if drawing
            text_choose.setText(sentence+ '\n 1' + choose_A + '\n 2 '+ choose_B + '\n 3 ' + choose_C + '\n 4 ' + choose_D, log=False)
        
        # *key_choose* updates
        waitOnFlip = False
        if key_choose.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_choose.frameNStart = frameN  # exact frame index
            key_choose.tStart = t  # local t and not account for scr refresh
            key_choose.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_choose, 'tStartRefresh')  # time at next scr refresh
            key_choose.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_choose.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_choose.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_choose.status == STARTED and not waitOnFlip:
            theseKeys = key_choose.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_choose.keys = theseKeys.name  # just the last key pressed
                key_choose.rt = theseKeys.rt
                # was this 'correct'?
                if (key_choose.keys == str(correctAns)) or (key_choose.keys == correctAns):
                    key_choose.corr = 1
                else:
                    key_choose.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_chooseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_choose"-------
    for thisComponent in trial_chooseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_choose.started', text_choose.tStartRefresh)
    trials.addData('text_choose.stopped', text_choose.tStopRefresh)
    # check responses
    if key_choose.keys in ['', [], None]:  # No response was made
        key_choose.keys = None
        # was no response the correct answer?!
        if str(correctAns).lower() == 'none':
           key_choose.corr = 1;  # correct non-response
        else:
           key_choose.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_choose.keys',key_choose.keys)
    trials.addData('key_choose.corr', key_choose.corr)
    if key_choose.keys != None:  # we had a response
        trials.addData('key_choose.rt', key_choose.rt)
    trials.addData('key_choose.started', key_choose.tStartRefresh)
    trials.addData('key_choose.stopped', key_choose.tStopRefresh)
    # the Routine "trial_choose" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "end"-------
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [text_2]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
end = timer.getTime()
duration = end - begin
'show %0.3f' %(duration)
end = timer.getTime()
duration = end - begin
'show %0.3f' %(duration)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
