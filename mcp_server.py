class MCPServer:
    """
    The Multi-agent Control Program (MCP) Server.
    This class orchestrates the workflow between different specialized AI agents.
    It has been refactored to allow for step-by-step execution for a UI.
    """

    def __init__(self):
        """
        Initializes the agents.
        """
        self.researcher = ResearcherAgent()
        self.financial_analyst = FinancialAnalystAgent()
        self.strategist = StrategistAgent()
        print("Agents initialized successfully.")

    def run_research_step(self, topic: str) -> str:
        """
        Executes only the research step.
        :param topic: The topic to research.
        :return: The research report.
        """
        prompt = f"Please provide a detailed research report on the company: '{topic}'."
        report = self.researcher.execute_task(prompt)
        return report

    def run_financial_analysis_step(self, research_report: str, topic: str) -> str:
        """
        Executes only the financial analysis step.
        :param research_report: The research report.
        :param topic: The company to analyze.
        :return: The financial analysis.
        """
        prompt = (
            f"Based on the following research report, provide a financial summary for {topic}.\n\n"
            f"--- Research Report ---\n{research_report}"
        )
        analysis = self.financial_analyst.execute_task(prompt)
        return analysis

    def run_strategy_step(self, research_report: str, financial_analysis: str, topic: str) -> str:
        """
        Executes only the final strategy (SWOT) step.
        :param research_report: The research report.
        :param financial_analysis: The financial analysis.
        :param topic: The company to analyze.
        :return: The SWOT analysis.
        """
        prompt = (
            f"Please create a SWOT analysis for {topic} based on the following reports.\n\n"
            f"--- Research Report ---\n{research_report}\n\n"
            f"--- Financial Analysis ---\n{financial_analysis}"
        )
        swot = self.strategist.execute_task(prompt)
        return swot
