from batch.trend_proposer import TrendProposer


def test_trend_proposer_dry_run() -> None:
    proposer = TrendProposer(api_key=None)
    keywords = proposer.propose(["AI"], limit=2, dry_run=True)
    assert len(keywords) == 2

