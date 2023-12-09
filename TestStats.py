class TestStats:
  def __init__(self):
    self._wpm = None
    self._accuracy = None
    self._time_taken = None

  def setWPM(self, wpm: float):
    self._wpm = wpm
    return self

  def setAccuracy(self, accuracy: float):
    self._accuracy = accuracy
    return self
  
  def setTimeTaken(self, time_taken: float):
    self._time_taken = time_taken
    return self
  
  def getWPM(self) -> float:
    return self._wpm
  
  def getAccuracy(self) -> float:
    return self._accuracy
  
  def getTimeTaken(self) -> float:
    return self._time_taken