# LTK - Copyrights Reserved 2023 - chrislaffra.com - See LICENSE 

import ltk
import ltk.pubsub
import random

fan = ltk.Preformatted("")

ltk.pubsub.subscribe(
    "Fan",           # the receiver
    "message",       # the subscription topic
    fan.append       # the handler to call
)

@ltk.callback
def publish(event=None):
    message = random.choice([
        "Subscribe!\n", "Like!\n", "Share!\n", "Pay me!\n", "Repost!\n"
    ]) 
    ltk.pubsub.publish(
        "Influencer",   # the sender
        "message",      # the subscription topic
        message         # the message to send 
    )

def create():
    return (
        ltk.VBox(
            ltk.H1("PubSub Demo"),
            ltk.Bold("The Influencer:"),
            ltk.Container(
                ltk.Button("Send a message", publish).css("margin-top", 5),
            ).css("margin-bottom", 25),

            ltk.Bold("What every fan sees:"),
            ltk.HBox(
                fan
                    .css("border", "1px solid gray")
                    .css("overflow", "hidden")
                    .css("width", 200)
                    .css("height", 400)
                    .css("margin-top", 5)
                    .addClass("fan"),
            ),
        )
        .attr("name", "PubSub")
    )
