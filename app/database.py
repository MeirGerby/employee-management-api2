from models import MissionResponse
from datetime import datetime, timedelta,timezone
from typing import Optional, List



class Database:
    def __init__(self):
        self.missions: List[MissionResponse] = []
        self.init_sample_data()

    def add_mission(self, mission: MissionResponse) -> MissionResponse:
        self.missions.append(mission)
        return mission

    def get_all_missions(self) -> List[MissionResponse]:
        return self.missions

    def get_mission_by_id(self, mission_id: int) -> Optional[MissionResponse]:
        for mission in self.missions:
            if mission.id == mission_id:
                return mission
        return None

    def get_missions_by_employee(self, emp_id: int) -> List[MissionResponse]:
        for m in self.missions:
            if m.assigned_to == emp_id:
                return m

    def update_mission(self, mission_id: int, data: dict) -> Optional[MissionResponse]:
        mission = self.get_mission_by_id(mission_id)
        if not mission:
            return None

        updated_data = mission.model_dump()
        updated_data.update(data)

        updated_mission = MissionResponse(**updated_data)
        index = self.missions.index(mission)
        self.missions[index] = updated_mission

        return updated_mission

    def delete_mission(self, mission_id: int) -> bool:
        mission = self.get_mission_by_id(mission_id)
        if not mission:
            return False

        self.missions.remove(mission)
        return True

    def init_sample_data(self):
        now = datetime.now(timezone.utc)

        self.missions = [
            MissionResponse(
                id=1,
                title="Prepare quarterly report",
                assigned_to=101,
                status="open",
                priority=1,
                deadline=now + timedelta(days=7),
                created_at=now,
            ),
            MissionResponse(
                id=2,
                title="Fix login bug",
                assigned_to=102,
                status="in_progress",
                priority=2,
                deadline=now + timedelta(days=3),
                created_at=now,
            ),
            MissionResponse(
                id=3,
                title="Deploy new version",
                assigned_to=101,
                status="pending",
                priority=1,
                deadline=now + timedelta(days=10),
                created_at=now,
            ),
            MissionResponse(
                id=4,
                title="Update documentation",
                assigned_to=103,
                status="open",
                priority=3,
                deadline=now + timedelta(days=14),
                created_at=now,
            ),
        ]
