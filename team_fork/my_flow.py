from prefect import flow, task, pause_flow_run
import random


@task()
def estimate_cost():
    cost = random.randint(999, 1_000_000)
    return cost

@flow(log_prints = True)
def expensive_ml_flow():
    cost = estimate_cost()
    if cost > 1000:
        print("This is a big cost!")
        approval = pause_flow_run(wait_for_input=bool)
        if not approval:
            print("I'm not made of money.")
            return False
    print("I'm doing the expensive ML model now!")

if __name__ == "__main__":
    expensive_ml_flow()