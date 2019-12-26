/************* 
 * Test Test *
 *************/

// init psychoJS:
var psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'test';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(instructionsRoutineBegin);
flowScheduler.add(instructionsRoutineEachFrame);
flowScheduler.add(instructionsRoutineEnd);
flowScheduler.add(sample_beginRoutineBegin);
flowScheduler.add(sample_beginRoutineEachFrame);
flowScheduler.add(sample_beginRoutineEnd);
const trials_2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_2LoopBegin, trials_2LoopScheduler);
flowScheduler.add(trials_2LoopScheduler);
flowScheduler.add(trials_2LoopEnd);
flowScheduler.add(session_beginRoutineBegin);
flowScheduler.add(session_beginRoutineEachFrame);
flowScheduler.add(session_beginRoutineEnd);
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(endRoutineBegin);
flowScheduler.add(endRoutineEachFrame);
flowScheduler.add(endRoutineEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({expName, expInfo});

var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '3.2.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0/Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0/60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}

var instructionsClock;
var ins;
var ins_key;
var sample_beginClock;
var text_sample;
var key_resp_2;
var trial_readtimeClock;
var text_readtime;
var test_key;
var trial_chooseClock;
var text_choose;
var key_choose;
var session_beginClock;
var text_begin;
var key_resp;
var endClock;
var text_2;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "instructions"
  instructionsClock = new util.Clock();
  ins = new visual.TextStim({
    win: psychoJS.window,
    name: 'ins',
    text: 'In this lab, you will see a block of text come up on the screen. You are asked to read out aloud the text and press Enter when you are done. After each text, you will be asked one question about the text that you just read. You will be given 4 choices for each question, please select the right answer by pressing the appropriate number key. You will get a break after 10 texts, you can press the Enter button if you want to skip that break. \n',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  ins_key = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "sample_begin"
  sample_beginClock = new util.Clock();
  text_sample = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_sample',
    text: 'sample begins\npress return',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial_readtime"
  trial_readtimeClock = new util.Clock();
  text_readtime = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_readtime',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  test_key = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial_choose"
  trial_chooseClock = new util.Clock();
  text_choose = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_choose',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_choose = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "session_begin"
  session_beginClock = new util.Clock();
  text_begin = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_begin',
    text: 'session begins\npress return',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial_readtime"
  trial_readtimeClock = new util.Clock();
  text_readtime = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_readtime',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  test_key = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial_choose"
  trial_chooseClock = new util.Clock();
  text_choose = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_choose',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_choose = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "end"
  endClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'end',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

var t;
var frameN;
var instructionsComponents;
function instructionsRoutineBegin() {
  //------Prepare to start Routine 'instructions'-------
  t = 0;
  instructionsClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  ins_key.keys = undefined;
  ins_key.rt = undefined;
  // keep track of which components have finished
  instructionsComponents = [];
  instructionsComponents.push(ins);
  instructionsComponents.push(ins_key);
  
  instructionsComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

var continueRoutine;
function instructionsRoutineEachFrame() {
  //------Loop for each frame of Routine 'instructions'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instructionsClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *ins* updates
  if (t >= 0.0 && ins.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    ins.tStart = t;  // (not accounting for frame time here)
    ins.frameNStart = frameN;  // exact frame index
    ins.setAutoDraw(true);
  }

  
  // *ins_key* updates
  if (t >= 0.0 && ins_key.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    ins_key.tStart = t;  // (not accounting for frame time here)
    ins_key.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { ins_key.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { ins_key.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { ins_key.clearEvents(); });
  }

  if (ins_key.status === PsychoJS.Status.STARTED) {
    let theseKeys = ins_key.getKeys({keyList: ['return'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  instructionsComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function instructionsRoutineEnd() {
  //------Ending Routine 'instructions'-------
  instructionsComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // the Routine "instructions" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var sample_beginComponents;
function sample_beginRoutineBegin() {
  //------Prepare to start Routine 'sample_begin'-------
  t = 0;
  sample_beginClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  key_resp_2.keys = undefined;
  key_resp_2.rt = undefined;
  // keep track of which components have finished
  sample_beginComponents = [];
  sample_beginComponents.push(text_sample);
  sample_beginComponents.push(key_resp_2);
  
  sample_beginComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function sample_beginRoutineEachFrame() {
  //------Loop for each frame of Routine 'sample_begin'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = sample_beginClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_sample* updates
  if (t >= 0.0 && text_sample.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_sample.tStart = t;  // (not accounting for frame time here)
    text_sample.frameNStart = frameN;  // exact frame index
    text_sample.setAutoDraw(true);
  }

  
  // *key_resp_2* updates
  if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_2.tStart = t;  // (not accounting for frame time here)
    key_resp_2.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
  }

  if (key_resp_2.status === PsychoJS.Status.STARTED) {
    let theseKeys = key_resp_2.getKeys({keyList: ['return'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      key_resp_2.keys = theseKeys[0].name;  // just the last key pressed
      key_resp_2.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  sample_beginComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function sample_beginRoutineEnd() {
  //------Ending Routine 'sample_begin'-------
  sample_beginComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
  if (typeof key_resp_2.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
      routineTimer.reset();
      }
  
  key_resp_2.stop();
  // the Routine "sample_begin" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var trials_2;
var currentLoop;
var trialIterator;
function trials_2LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'sample_test.xlsx',
    seed: undefined, name: 'trials_2'});
  psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
  currentLoop = trials_2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = trials_2[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial_2 = result.value;
    thisScheduler.add(importConditions(trials_2));
    thisScheduler.add(trial_readtimeRoutineBegin);
    thisScheduler.add(trial_readtimeRoutineEachFrame);
    thisScheduler.add(trial_readtimeRoutineEnd);
    thisScheduler.add(trial_chooseRoutineBegin);
    thisScheduler.add(trial_chooseRoutineEachFrame);
    thisScheduler.add(trial_chooseRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}


function trials_2LoopEnd() {
  psychoJS.experiment.removeLoop(trials_2);

  return Scheduler.Event.NEXT;
}

var trials;
function trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'test.xlsx',
    seed: undefined, name: 'trials'});
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = trials[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial = result.value;
    thisScheduler.add(importConditions(trials));
    thisScheduler.add(trial_readtimeRoutineBegin);
    thisScheduler.add(trial_readtimeRoutineEachFrame);
    thisScheduler.add(trial_readtimeRoutineEnd);
    thisScheduler.add(trial_chooseRoutineBegin);
    thisScheduler.add(trial_chooseRoutineEachFrame);
    thisScheduler.add(trial_chooseRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}

var trial_readtimeComponents;
function trial_readtimeRoutineBegin() {
  //------Prepare to start Routine 'trial_readtime'-------
  t = 0;
  trial_readtimeClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  text_readtime.setText(sentence);
  test_key.keys = undefined;
  test_key.rt = undefined;
  // keep track of which components have finished
  trial_readtimeComponents = [];
  trial_readtimeComponents.push(text_readtime);
  trial_readtimeComponents.push(test_key);
  
  trial_readtimeComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function trial_readtimeRoutineEachFrame() {
  //------Loop for each frame of Routine 'trial_readtime'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = trial_readtimeClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_readtime* updates
  if (t >= 0.0 && text_readtime.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_readtime.tStart = t;  // (not accounting for frame time here)
    text_readtime.frameNStart = frameN;  // exact frame index
    text_readtime.setAutoDraw(true);
  }

  
  // *test_key* updates
  if (t >= 0.0 && test_key.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    test_key.tStart = t;  // (not accounting for frame time here)
    test_key.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { test_key.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { test_key.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { test_key.clearEvents(); });
  }

  if (test_key.status === PsychoJS.Status.STARTED) {
    let theseKeys = test_key.getKeys({keyList: ['return'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      test_key.keys = theseKeys[0].name;  // just the last key pressed
      test_key.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  trial_readtimeComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function trial_readtimeRoutineEnd() {
  //------Ending Routine 'trial_readtime'-------
  trial_readtimeComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('test_key.keys', test_key.keys);
  if (typeof test_key.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('test_key.rt', test_key.rt);
      routineTimer.reset();
      }
  
  test_key.stop();
  // the Routine "trial_readtime" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var trial_chooseComponents;
function trial_chooseRoutineBegin() {
  //------Prepare to start Routine 'trial_choose'-------
  t = 0;
  trial_chooseClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  key_choose.keys = undefined;
  key_choose.rt = undefined;
  // keep track of which components have finished
  trial_chooseComponents = [];
  trial_chooseComponents.push(text_choose);
  trial_chooseComponents.push(key_choose);
  
  trial_chooseComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function trial_chooseRoutineEachFrame() {
  //------Loop for each frame of Routine 'trial_choose'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = trial_chooseClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_choose* updates
  if (t >= 0.0 && text_choose.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_choose.tStart = t;  // (not accounting for frame time here)
    text_choose.frameNStart = frameN;  // exact frame index
    text_choose.setAutoDraw(true);
  }

  
  if (text_choose.status === PsychoJS.Status.STARTED){ // only update if being drawn
    text_choose.setText(((((((((sentence + '\n 1') + choose_A) + '\n 2 ') + choose_B) + '\n 3 ') + choose_C) + '\n 4 ') + choose_D));
  }
  
  // *key_choose* updates
  if (t >= 0.0 && key_choose.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_choose.tStart = t;  // (not accounting for frame time here)
    key_choose.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_choose.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { key_choose.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { key_choose.clearEvents(); });
  }

  if (key_choose.status === PsychoJS.Status.STARTED) {
    let theseKeys = key_choose.getKeys({keyList: ['1', '2', '3', '4'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      key_choose.keys = theseKeys[0].name;  // just the last key pressed
      key_choose.rt = theseKeys[0].rt;
      // was this 'correct'?
      if (key_choose.keys === correctAns) {
          key_choose.corr = 1;
      } else {
          key_choose.corr = 0;
      }
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  trial_chooseComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function trial_chooseRoutineEnd() {
  //------Ending Routine 'trial_choose'-------
  trial_chooseComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // was no response the correct answer?!
  if (key_choose.keys === undefined) {
    if (['None','none',undefined].includes(correctAns)) {
       key_choose.corr = 1  // correct non-response
    } else {
       key_choose.corr = 0  // failed to respond (incorrectly)
    }
  }
  // store data for thisExp (ExperimentHandler)
  psychoJS.experiment.addData('key_choose.keys', key_choose.keys);
  psychoJS.experiment.addData('key_choose.corr', key_choose.corr);
  if (typeof key_choose.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('key_choose.rt', key_choose.rt);
      routineTimer.reset();
      }
  
  key_choose.stop();
  // the Routine "trial_choose" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var session_beginComponents;
function session_beginRoutineBegin() {
  //------Prepare to start Routine 'session_begin'-------
  t = 0;
  session_beginClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  key_resp.keys = undefined;
  key_resp.rt = undefined;
  // keep track of which components have finished
  session_beginComponents = [];
  session_beginComponents.push(text_begin);
  session_beginComponents.push(key_resp);
  
  session_beginComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function session_beginRoutineEachFrame() {
  //------Loop for each frame of Routine 'session_begin'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = session_beginClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_begin* updates
  if (t >= 0.0 && text_begin.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_begin.tStart = t;  // (not accounting for frame time here)
    text_begin.frameNStart = frameN;  // exact frame index
    text_begin.setAutoDraw(true);
  }

  
  // *key_resp* updates
  if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp.tStart = t;  // (not accounting for frame time here)
    key_resp.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
  }

  if (key_resp.status === PsychoJS.Status.STARTED) {
    let theseKeys = key_resp.getKeys({keyList: ['return'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      key_resp.keys = theseKeys[0].name;  // just the last key pressed
      key_resp.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  session_beginComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function session_beginRoutineEnd() {
  //------Ending Routine 'session_begin'-------
  session_beginComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
  if (typeof key_resp.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
      routineTimer.reset();
      }
  
  key_resp.stop();
  // the Routine "session_begin" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var endComponents;
function endRoutineBegin() {
  //------Prepare to start Routine 'end'-------
  t = 0;
  endClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // keep track of which components have finished
  endComponents = [];
  endComponents.push(text_2);
  
  endComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function endRoutineEachFrame() {
  //------Loop for each frame of Routine 'end'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = endClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_2* updates
  if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_2.tStart = t;  // (not accounting for frame time here)
    text_2.frameNStart = frameN;  // exact frame index
    text_2.setAutoDraw(true);
  }

  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  endComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function endRoutineEnd() {
  //------Ending Routine 'end'-------
  endComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // the Routine "end" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}


function endLoopIteration({thisScheduler, isTrials=true}) {
  // ------Prepare for next entry------
  return function () {
    // ------Check if user ended loop early------
    if (currentLoop.finished) {
      // Check for and save orphaned data
      if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
        psychoJS.experiment.nextEntry();
      }
      thisScheduler.stop();
    } else if (isTrials) {
      psychoJS.experiment.nextEntry();
    }
  return Scheduler.Event.NEXT;
  };
}


function importConditions(loop) {
  const trialIndex = loop.getTrialIndex();
  return function () {
    loop.setTrialIndex(trialIndex);
    psychoJS.importAttributes(loop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});

  return Scheduler.Event.QUIT;
}
