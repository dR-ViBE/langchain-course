import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq 
load_dotenv()


def main():
    print("Hello from langchain-course!")
    # print(os.environ.get("GROQ_API_KEY"))
    information=""" Lionel Andrés "Leo" Messi[note 1] (Spanish: [ljoˈnel anˈdɾes ˈmesi] ⓘ; born 24 June 1987) is an Argentine professional footballer who plays as a forward for and captains both Major League Soccer club Inter Miami and the Argentina national team. Widely regarded as one of the greatest players in history, Messi has set numerous records for individual accolades won throughout his professional footballing career, including eight Ballon d'Ors, six European Golden Shoes, and eight times being named the world's best player by FIFA.[note 2] In 2025, he was named the All Time Men's World Best Player by the IFFHS. He is the most decorated player in the history of professional football having won 45 team trophies.[note 3] Messi's records include most goals in a calendar year (91), most goals for a single club (672 for Barcelona), most goals in La Liga (474), most assists in international football (60), most goal contributions in the FIFA World Cup (21), and most goal contributions in the Copa América (32). A prolific goalscorer and creative playmaker, Messi has scored over 890 senior career goals and provided over 390 assists for club and country—the most of any player—resulting in over 1,290 goal contributions, the highest total in the sport's history.[21]

Messi made his competitive debut for Barcelona at age 17 in October 2004. He gradually established himself as an integral player for the club, and during his first uninterrupted season at age 22 in 2008–09 he helped Barcelona achieve the first treble in Spanish football. This resulted in Messi winning the first of four consecutive Ballon d'Ors, and by the 2011–12 season he set the European record for most goals in a season and established himself as Barcelona's all-time top scorer. During the 2014–15 campaign, where he became the all-time top scorer in La Liga, he led Barcelona to a historic second treble, leading to a fifth Ballon d'Or in 2015. He assumed Barcelona's captaincy in 2018 and won a record sixth Ballon d'Or in 2019. At Barcelona, Messi won a club-record 34 trophies, including ten La Liga titles and four Champions Leagues, among others. Financial difficulties at Barcelona led to Messi signing with French club Paris Saint-Germain in August 2021, where he won the Ligue 1 title during both of his seasons there. He joined MLS club Inter Miami in July 2023."""
    summary_template="""give information {information} about a person i want you to create:
     1. About summary
      2.two intresting facts about them"""
    
    summary_prompt_template=PromptTemplate(
        input_variables={information},template=summary_template
    )

    llm=ChatGroq(temperature=0,model="llama-3.1-8b-instant")
    chain=summary_prompt_template | llm
    response=chain.invoke(input={"information": information})
    print(response.content)
if __name__ == "__main__":
    main()
