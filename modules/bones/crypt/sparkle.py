import modules.bones.crypt.switch as Switch
import modules.bones.crypt.sugar as Sugar
import modules.bones.crypt.hashing as Hash

# Encrypt


def Encrypt(text, key):

    sugar = Hash.getSugarByKey(key, text)
    sugaryText = Sugar.addSugar(text, sugar)
    switchedText = Switch.encode(sugaryText, key)
    return switchedText

# Decrypt


def Decrypt(text, key):
    switchBack = Switch.decode(text, key)
    sugar = Hash.getSugarByKey(key, switchBack)
    deswitchData = Sugar.removeSugar(switchBack, sugar)
    return deswitchData
