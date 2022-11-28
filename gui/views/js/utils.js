const askForFile = async () => {
  return await eel.ask_file()();
};

const submitIUTPath = async (image_path) => {
  return await eel.submit_iut_path(image_path)();
}

const doMotionDeblur = async (angle=135, strength=22, snr=25, iut_already_displayed=false) => {
  return await eel.do_motion_deblur(angle, strength, snr, iut_already_displayed)();
}
