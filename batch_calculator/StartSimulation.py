import time

from openapi_client import SimulationsApi
from openapi_client.models.simulation import Simulation


class StartSimulation:
    def __init__(self, client, model_id, model_name, organisation_id, bui_info):
        self._client = client
        self._sim = SimulationsApi(client)

        self.model_id = model_id
        self.organisation_id = organisation_id
        self.sim_name = model_name + "_" + bui_info.start_datetime
        self.duration = bui_info.duration

        my_sim = Simulation(
            name=self.sim_name,
            threedimodel=self.model_id,
            organisation=self.organisation_id,
            start_datetime=bui_info.start_datetime,
            duration=int(bui_info.duration),
        )

        sim = self._sim.simulations_create(my_sim)
        self.created_sim_id = sim.id
        self.sim_id_value = str(self.created_sim_id)

        print("curr_sim_id: " + self.sim_id_value)

        sim_start = self._sim.simulations_actions_create(
            simulation_pk=self.created_sim_id, data={"name": "start"}
        )

        status = self._sim.simulations_status_list(self.created_sim_id, async_req=False)
        print(status.name, end="\r", flush=True)
        # while status.name != "initialized":
        while status.name == "starting":
            print(status.name, end="\r", flush=True)
            status = self._sim.simulations_status_list(
                self.created_sim_id, async_req=False
            )
            time.sleep(5.0)

        progress = self._sim.simulations_progress_list(
            self.created_sim_id, async_req=False
        )

        while progress.percentage < 100:
            progress = self._sim.simulations_progress_list(
                self.created_sim_id, async_req=False
            )

            print(progress.percentage, end="\r", flush=True)
            time.sleep(1.0)
