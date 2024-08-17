import pickle
import threading
from argparse import ArgumentParser

from pynput.keyboard import Key

import controller
from agent import MineRLAgent
from killer import listen_exit_key
from lib.screenshot import screenshot
from loguru import logger


@listen_exit_key(Key.esc)
def main(model, weights, keyboard_interrupt_event: threading.Event = None):
    print("---Loading model---")
    agent_parameters = pickle.load(open(model, "rb"))
    policy_kwargs = agent_parameters["model"]["args"]["net"]["args"]
    pi_head_kwargs = agent_parameters["model"]["args"]["pi_head_opts"]
    pi_head_kwargs["temperature"] = float(pi_head_kwargs["temperature"])
    agent = MineRLAgent(policy_kwargs=policy_kwargs, pi_head_kwargs=pi_head_kwargs)
    agent.load_weights(weights)

    print("---Launching MineRL enviroment (be patient)---")

    while True:
        if keyboard_interrupt_event.is_set():
            raise KeyboardInterrupt()
        # @AkagawaTsurunaki
        # This is the screenshot from observation
        # The tensor must have shape [1, 128, 128, 3]
        # assert agent_input['img'].shape == th.Size([1, 128, 128, 3])
        agent_input = {
            "img": screenshot.capture().to("cuda")
        }
        minerl_action: dict = agent.get_action(agent_input)
        logger.info(minerl_action)
        controller.minerl_action_to_env(minerl_action)


if __name__ == "__main__":
    parser = ArgumentParser("Run pretrained models on MineRL environment")

    parser.add_argument("--weights", type=str, required=True, help="Path to the '.weights' file to be loaded.")
    parser.add_argument("--model", type=str, required=True, help="Path to the '.model' file to be loaded.")

    args = parser.parse_args()

    main(args.model, args.weights)
