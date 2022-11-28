const askForFile = async () => {
  return await eel.ask_file()();
};

const doMotionDeblur = async (image_path, angle=135, strength=22, snr=25, iut_already_displayed=false) => {
  return await eel.do_motion_deblur(image_path, angle, strength, snr, iut_already_displayed)();
}
