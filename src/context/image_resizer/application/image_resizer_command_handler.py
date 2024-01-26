from context.image_resizer.application.image_resizer_command import ImageResizerCommand


class ImageResizerCommandHandler():
    def __init__(self, creator: ImageResizerCreator):
        self._creator = creator

    def __call__(self, command: ImageResizerCommand):
        self._