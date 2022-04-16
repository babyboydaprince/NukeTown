import modules.jackphone.requestSender as request
import modules.jackphone.dataRandomizer as randomData

__services = request.getServices()


def flood(target):
    # Get services list
    service = randomData.random_service(__services)
    service = request.Service(service)
    service.sendMessage(target)
