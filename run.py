from app import create_app


APP = create_app({'DEBUG': True})


if __name__ == '__main__':
    APP.run()
