const askForFile = async () => {
  return await eel.ask_file()();
};

const doMotionDeblur = async (image_path, angle=135, strength=22, snr=25) => {
  return await eel.motion_deblur(image_path, angle, strength, snr)();
}
