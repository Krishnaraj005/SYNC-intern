from plyer import notification
title = 'Work Alert....'
message = 'Its time to Work!!!'

notification.notify(title=title,
                    message=message,
                    app_icon=None,
                    timeout=10,
                    toast=False)