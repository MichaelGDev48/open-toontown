from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectGlobalAI import DistributedObjectGlobalAI
from direct.distributed.PyDatagram import *


class ToontownFriendsManagerAI(DistributedObjectGlobalAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToontownFriendsManagerAI')

    def sendFriendOnline(self, avId, friendId, commonChatFlags, whitelistChatFlags):
        self.sendUpdateToAvatarId(avId, 'friendOnline', [friendId, commonChatFlags, whitelistChatFlags])

    def sendMakeFriends(self, avatarAId, avatarBId, flags, context):
        self.sendUpdate('makeFriends', [avatarAId, avatarBId, flags, context])

    def makeFriendsResponse(self, avatarAId, avatarBId, result, context):
        if result == 1:
            avatarA = self.air.doId2do.get(avatarAId)
            avatarB = self.air.doId2do.get(avatarBId)
            if avatarA and avatarB:
                self.sendFriendOnline(avatarAId, avatarBId, 0, 1)
                self.sendFriendOnline(avatarBId, avatarAId, 0, 1)

        messenger.send("makeFriendsReply", [result, context])

    def requestSecretResponse(self, result, secret, avId):
        messenger.send("requestSecretReply", [result, secret, avId])

    def sendRequestSecret(self, requesterId):
        self.sendUpdate('requestSecret', [requesterId])

    def sendSubmitSecret(self, avId, secret):
        self.sendUpdate('submitSecret', [avId, secret])

    def submitSecretResponse(self, result, recipient, requesterId):
        messenger.send("submitSecretReply", [result, recipient, requesterId])