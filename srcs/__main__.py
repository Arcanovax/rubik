from ursina import (Ursina,
                    camera,
                    window,
                    Vec3,
                    DirectionalLight,
                    AmbientLight,
                    color,
                    Entity,EditorCamera)

from .enum import Color_code


def get_face(i, letter):
    e = Entity(model='plane', position=(i%3, 0, i//3), color=Color_code[letter].value, scale=0.9)


def main() -> None:
    """Main function
    """
    try:
        app = Ursina()
        window.exit_button.enabled = False
        camera.fov = 120
        camera.position = Vec3(0, 5, -10)

        cube = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"
        for i in range(len(cube)):
            get_face(i, cube[i])

        EditorCamera()
        app.run()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
