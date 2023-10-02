gpt_direct_suggestions_system_message = "You're a trip planner, tour guide, and behavioral expert with 20 years of " \
                                        "experience. Users will give you some criteria (including their Myers Briggs " \
                                        "Personality Type) and ask you to plan an activity for a certain time and " \
                                        "area. Your job is create 10 recommendations for this user. "
gpt_rewrite_excerpt_system_message = "You're a helpful assistant who will be given a list of titles and excerpts from"\
                                     "websites that signify activities. Briefly create new excerpts for each website" \
                                     "that will effectively market the activity. Do not make up any information that " \
                                     "you're not given. Return only the list of excerpt in bullet format and " \
                                     "nothing else. Keep each response to under 50 words."

gpt_summarize_activities_system_message = "Given a user's personality type, preference for type of activity that he " \
                                          "would like to do, and 15 activities that correlate to his personality and " \
                                          "preferences, summarize the type of activities into a very brief single " \
                                          "paragraph and mention in one sentence why the user will enjoy them. Keep " \
                                          "your response under 150 words."


def metaphor_direct_suggestions_prompt(inputs):
    """
    Create a prompt for metaphor's neural search which can be used to generate activity suggestions
    based on preferences presented inputs

    :param inputs:
    :return:
    """
    # Over/under 21 string
    if inputs['over_21'] == "true":
        age = "over 21"
    else:
        age = "under 21"

    # Number of people string
    if inputs['number_of_people'] == "1":
        number_of_people = "just myself"
    else:
        number_of_people = f"{inputs['number_of_people']} people and myself"

    # Combine filters together
    filters_string = ""
    for item in inputs['filters']:
        filters_string += f"{item}, "

    if filters_string == "":
        return f"I'm a {inputs['personality_type']} Myers-Briggs personality who's {age} and was looking for an " \
               f"{inputs['indoor_or_outdoor']} {inputs['social']} activity on {inputs['date']} {inputs['time']} for " \
               f"{number_of_people} in {inputs['location']}. This place gave me the best " \
               f"{inputs['type_of_activity']} experience:"
    else:
        return f"I'm a {inputs['personality_type']} Myers-Briggs personality who's {age} and was looking for an " \
               f"{inputs['indoor_or_outdoor']} {inputs['social']} activity on {inputs['date']} {inputs['time']} for " \
               f"{number_of_people} in {inputs['location']}. This place with {filters_string}gave me the best " \
               f"{inputs['type_of_activity']} experience:"

    # Second version of the prompt provided by GPT-4. Refine it before using it!
    # return f"Being an {inputs['personality_type']} and wanting a '{inputs['type_of_activity']}' "
    #     f"experience, I was looking for a spot where I could spend a {inputs['social']} {sample_input_1['time']}"
    #     f"on {inputs['date']} in the {inputs['location']}. Though it's for just "
    #     f"{inputs['number_of_people']} person and in an {inputs['indoor_or_outdoor']} setting, "
    #     f"I wanted it to be exclusive for those over 21 ({inputs['over_21']}), but with certain "
    #     f"conditions like {', '.join(inputs['filters'])}. The place I found was absolutely perfect:"


def gpt_direct_suggestions_prompt(inputs):
    """
    Create a prompt for GPT-3 which can be used to generate activity suggestions based on preferences.
    This prompt will NOT take into account location and time preferences as expressed in inputs. Use
    recommendations from this prompt and search using Metaphor's neural search to find location specific
    recommendations.

    :param inputs:
    :return:
    """
    # Over/under 21 string
    if inputs['over_21'] == "true":
        age = "over 21"
    else:
        age = "under 21"

    # Number of people string
    if inputs['number_of_people'] == "1":
        number_of_people = "just myself"
    else:
        number_of_people = f"{inputs['number_of_people']} people and myself"

    filters_string = ""
    for item in inputs['filters']:
        filters_string += f"{item}, "

    if filters_string == "":
        return f"I'm a {inputs['personality_type']} Myers-Briggs personality who's {age} and am looking for an " \
               f"{inputs['indoor_or_outdoor']} {inputs['social']} activity for {number_of_people} in " \
               f"{inputs['location']}. This place should give me the best high-energy {inputs['type_of_activity']} " \
               f"experience. What would you recommend? Respond with only the recommendation in a bullet list form" \
               f"and nothing else."
    else:
        return f"I'm a {inputs['personality_type']} Myers-Briggs personality who's {age} and am looking for an " \
               f"{inputs['indoor_or_outdoor']} {inputs['social']} activity for {number_of_people} in " \
               f"{inputs['location']}. This place should include {filters_string}and give me the best high-energy " \
               f"{inputs['type_of_activity']} experience. What would you recommend? Respond with only the " \
               f"recommendation in a bullet list form and nothing else."


def gpt_output_recommendations_prompt(inputs, list_of_activities):
    """
    Take a list of ranked, location and preference informed suggestions of things to do and formulate a nice
    output for the user. Ensure to include the following:
    - A list of suggestions
    - A list of links to the suggestions
    - A list of descriptions of the suggestions
    - A list of images of the suggestions (TODO: NOT YET IMPLEMENTED)
    - A list of prices of the suggestions (TODO: NOT YET IMPLEMENTED)
    - A list of ratings of the suggestions (TODO: NOT YET IMPLEMENTED)
    - A list of reviews of the suggestions (TODO: NOT YET IMPLEMENTED)

    INCLUDE A DISCLAIMER THAT ACTIVITIES SHOULD FURTHER RESEARCH THE ACTIVITY FOR SECURITY AND DATA INTEGRITY (some
    search results returned by Metaphor may be old)

    :param inputs:
    :return:
    """
    return f"As a {inputs['personality_type']} Myers-Briggs personality who's looking for {inputs['type_of_activity']}" \
           f" here's a list of activities in {inputs['location']} that I think you'll enjoy:\n {list_of_activities}"


def gpt_output_personality_related_recommendations(inputs):
    """
    Based on input personality type, output what an ideal activity for that personality type would be.
    This was created based on prompting GPT-4 with the following:
        You are a behaviors expert. Briefly describe what the perfect evening out on the city would look like for each
        of the 16 Myers-Briggs personality types, write a short description of why that personality type may enjoy the
        activity.

    TODO: Would be nice to use input type to further curate the activity type.
        Ex. based on "type_of_activity" user input, ask gpt to generate an activity that is "cozy" and "intimate" for
        the given personality type.


    :param inputs:
    :return:
    """
    if inputs["personality_type"] == "ISTJ":
        return "Ideal Activity: A structured and planned-out activity. because ISTJs appreciate organization and " \
               "reliability. A well-organized activity, perhaps a dinner at a trusted restaurant followed by a " \
               "scheduled event, would make them feel comfortable and satisfied."
    elif inputs["personality_type"] == "ISFJ":
        return "Ideal activity: A cozy and intimate gathering because ISFJs value close relationships. A small " \
               "get-together with close friends or family at a quiet, cozy spot would appeal to their preference for " \
               "warm, meaningful interactions. "
    elif inputs["personality_type"] == "INFJ":
        return "Ideal activity: An intimate and deep conversation session because INFJs often seek depth in their " \
               "interactions. An activity spent in a serene setting, discussing life’s mysteries and personal " \
               "philosophies with a close friend, would be appealing. "
    elif inputs["personality_type"] == "INTJ":
        return "Ideal activity: A thought-provoking play or lecture because INTJs enjoy intellectual stimulation. An " \
               "activity attending a lecture, discussion panel, or play that offers depth and insight would engage " \
               "their analytical minds. "
    elif inputs["personality_type"] == "ISTP":
        return "Ideal activity: An adventurous activity because ISTPs tend to enjoy living on the edge. An activity " \
               "involving some form of physical activity or a spontaneous adventure would be thrilling for them. "
    elif inputs["personality_type"] == "ISFP":
        return "Ideal activity: An art exhibition or concert because ISFPs are drawn to aesthetic experiences. They " \
               "would enjoy an activity where they can immerse themselves in artistic expressions, be it visual arts " \
               "or musical performances. "
    elif inputs["personality_type"] == "INFP":
        return "Ideal activity: A quiet, creative workshop because INFPs value authenticity and self-expression. A " \
               "peaceful activity spent in a creative writing or art workshop, where they can express themselves " \
               "authentically, would be ideal. "
    elif inputs["personality_type"] == "INTP":
        return "Ideal activity: Attending a science or tech event because INTPs enjoy exploring ideas and theories. " \
               "An activity at a science talk, tech meetup, or a documentary screening would cater to their curious " \
               "minds. "
    elif inputs["personality_type"] == "ESTP":
        return "Ideal activity: A lively and bustling venue because ESTPs are energetic and sociable. A lively " \
               "environment, such as a concert, party, or any event with an upbeat atmosphere, would be exhilarating " \
               "for them. "
    elif inputs["personality_type"] == "ESFP":
        return "Ideal activity: A social gathering or event because ESFPs love engaging with others in a fun, " \
               "spirited manner. An activity at a vibrant, sociable event, such as a festival or party, " \
               "would be entertaining for them. "
    elif inputs["personality_type"] == "ENFP":
        return "Ideal activity: Exploring new and eclectic venues because ENFPs enjoy novelty and excitement. An " \
               "activity spent exploring various unique spots, perhaps a new thematic café or an unusual event, " \
               "would captivate their interest. "
    elif inputs["personality_type"] == "ENTP":
        return "Ideal activity: A debate or lively discussion group because ENTPs thrive in intellectually " \
               "stimulating environments. An activity spent debating or exploring various topics with a diverse group " \
               "of people would be stimulating for them. "
    elif inputs["personality_type"] == "ESTJ":
        return "Ideal activity: A traditional and established event because ESTJs often appreciate order and " \
               "tradition. Attending a classical music concert, a well-known play, or a reputable event would align " \
               "with their preferences."
    elif inputs["personality_type"] == "ESFJ":
        return "Ideal activity: Hosting a dinner party because ESFJs enjoy taking care of others and creating " \
               "harmonious environments. Hosting a dinner where they can connect people, foster relationships, and " \
               "ensure everyone is having a good time would be rewarding for them."
    elif inputs["personality_type"] == "ENFJ":
        return "Ideal activity: Organizing a charity event or gathering because ENFJs are naturally altruistic and " \
               "enjoy bringing people together for a cause. Organizing or attending a charity event where they can " \
               "socialize and contribute to a meaningful cause would be ideal."
    elif inputs["personality_type"] == "ENTJ":
        return "Ideal activity: Attending a high-profile event or networking session because ENTJs enjoy " \
               "opportunities where they can network, lead, and potentially further their ambitions. An activity at a " \
               "high-profile event or a professional networking session would cater to their strategic and social " \
               "inclinations. "
    else:
        raise Exception("Invalid personality type")
