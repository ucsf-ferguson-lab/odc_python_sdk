from dataclasses import dataclass


@dataclass
class StatEndpoints:
    """
    Create full endpoint url\n\n
    datasets_stats, users_stats, labs_stats, downloads_stats
    """

    datasets_stats: str
    users_stats: str
    labs_stats: str
    downloads_stats: str

    # base_url set by default with option to change as needed
    @classmethod
    def from_base_url(
        cls, base_url: str = "https://services.scicrunch.io/odc"
    ) -> "StatEndpoints":
        """Factory method to init all endpoints from base_url"""
        return cls(
            datasets_stats=f"{base_url}/stats/datasets",
            users_stats=f"{base_url}/stats/users",
            labs_stats=f"{base_url}/stats/labs",
            downloads_stats=f"{base_url}/stats/downloads",
        )
