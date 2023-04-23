# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import configparser
import json
import os

from flask import jsonify, render_template, request, Response

from backend.create_recaptcha_assessment import create_assessment

# Sample threshold score for classification of bad / not bad action. The threshold score
# can be used to trigger secondary actions like MFA.
SAMPLE_THRESHOLD_SCORE = 0.50

context = {
    "project_id": os.environ["GOOGLE_CLOUD_PROJECT"],
    "site_key": os.environ["SITE_KEY"],
}

# Parse config file and read available reCAPTCHA actions. All reCAPTCHA actions registered in the client
# should be mapped in the config file. This will be used to verify if the token obtained during assessment
# corresponds to the claimed action.
config = configparser.ConfigParser()
config.read("config.ini")
assert "recaptcha_actions" in config


# Return homepage template.
def home() -> str:
    return render_template(template_name_or_list="home.html", context=context)


# On homepage load, execute reCAPTCHA Enterprise assessment and take action according to the score.
def on_homepage_load() -> Response:
    try:
        recaptcha_action = config["recaptcha_actions"]["home"]
        json_data = json.loads(request.data)

        # <!-- ATTENTION: reCAPTCHA Example (Server Part 1/2) Starts -->
        assessment_response = create_assessment(
            context.get("project_id"),
            context.get("site_key"),
            json_data["token"],
        )

        # Check if the token is valid, score is above threshold score and the action equals expected.
        if assessment_response.token_properties.valid and \
                assessment_response.risk_analysis.score > SAMPLE_THRESHOLD_SCORE and \
                assessment_response.token_properties.action == recaptcha_action:
            # Load the home page.
            # Business logic.
            # Classify the action as not bad.
            verdict = "Not Bad"
        else:
            # If any of the above condition fails, trigger email/ phone verification flow.
            # Classify the action as bad.
            verdict = "Bad"
        # <!-- ATTENTION: reCAPTCHA Example (Server Part 1/2) Ends -->

        # Return the risk score.
        return jsonify(
            {
                "data": {
                    "score": "{:.1f}".format(assessment_response.risk_analysis.score),
                    "verdict": verdict,
                }
            }
        )
    except ValueError or Exception as e:
        return jsonify({"data": {"error_msg": str(e.__dict__)}})


# Return signup template.
def signup() -> str:
    return render_template(template_name_or_list="signup.html", context=context)


# On signup button click, execute reCAPTCHA Enterprise assessment and take action according to the score.
def on_signup() -> Response:
    try:
        recaptcha_action = config["recaptcha_actions"]["signup"]
        json_data = json.loads(request.data)

        # <!-- ATTENTION: reCAPTCHA Example (Server Part 1/2) Starts -->
        assessment_response = create_assessment(
            context.get("project_id"),
            context.get("site_key"),
            json_data["token"],
        )

        # Check if the token is valid, score is above threshold score and the action equals expected.
        if assessment_response.token_properties.valid and \
                assessment_response.risk_analysis.score > SAMPLE_THRESHOLD_SCORE and \
                assessment_response.token_properties.action == recaptcha_action:
            # Write new username and password to users database.
            # username = json_data["username"]
            # password = json_data["password"]
            # Business logic.
            # Classify the action as not bad.
            verdict = "Not Bad"
        else:
            # If any of the above condition fails, trigger email/ phone verification flow.
            # Classify the action as bad.
            verdict = "Bad"
        # <!-- ATTENTION: reCAPTCHA Example (Server Part 1/2) Ends -->

        # Return the risk score.
        return jsonify(
            {
                "data": {
                    "score": "{:.1f}".format(assessment_response.risk_analysis.score),
                    "verdict": verdict,
                }
            }
        )
    except ValueError or Exception as e:
        return jsonify({"data": {"error_msg": str(e.__dict__)}})


# Return login template.
def login() -> str:
    return render_template(template_name_or_list="login.html", context=context)


# On login button click, execute reCAPTCHA Enterprise assessment and take action according to the score.
def on_login() -> Response:
    try:
        recaptcha_action = config["recaptcha_actions"]["login"]
        json_data = json.loads(request.data)

        # <!-- ATTENTION: reCAPTCHA Example (Server Part 1/2) Starts -->
        assessment_response = create_assessment(
            context.get("project_id"),
            context.get("site_key"),
            json_data["token"],
        )

        # Check if the token is valid, score is above threshold score and the action equals expected.
        if assessment_response.token_properties.valid and \
                assessment_response.risk_analysis.score > SAMPLE_THRESHOLD_SCORE and \
                assessment_response.token_properties.action == recaptcha_action:
            # Check if the login credentials exist and match.
            # username = json_data["username"]
            # password = json_data["password"]
            # Business logic.
            # Classify the action as not bad.
            verdict = "Not Bad"
        else:
            # If any of the above condition fails, trigger email/phone verification flow.
            # Classify the action as bad.
            verdict = "Bad"
        # <!-- ATTENTION: reCAPTCHA Example (Server Part 1/2) Ends -->

        # Return the risk score.
        return jsonify(
            {
                "data": {
                    "score": "{:.1f}".format(assessment_response.risk_analysis.score),
                    "verdict": verdict,
                }
            }
        )
    except ValueError or Exception as e:
        return jsonify({"data": {"error_msg": str(e.__dict__)}})


# Return store template.
def store() -> str:
    return render_template(template_name_or_list="store.html", context=context)


# On checkout button click in store page, execute reCAPTCHA Enterprise assessment and take action according to the score.
def on_store_checkout() -> Response:
    try:
        recaptcha_action = config["recaptcha_actions"]["store"]
        json_data = json.loads(request.data)

        # <!-- ATTENTION: reCAPTCHA Example (Server Part 1/2) Starts -->
        assessment_response = create_assessment(
            context.get("project_id"),
            context.get("site_key"),
            json_data["token"],
        )

        # Check if the token is valid, score is above threshold score and the action equals expected.
        if assessment_response.token_properties.valid and \
                assessment_response.risk_analysis.score > SAMPLE_THRESHOLD_SCORE and \
                assessment_response.token_properties.action == recaptcha_action:
            # Check if the cart contains items and proceed to checkout and payment.
            # items = json_data["items"]
            # Business logic.
            # Classify the action as not bad.
            verdict = "Not Bad"
        else:
            # If any of the above condition fails, trigger email/phone verification flow.
            # Classify the action as bad.
            verdict = "Bad"
        # <!-- ATTENTION: reCAPTCHA Example (Server Part 1/2) Ends -->

        # Return the risk score.
        return jsonify(
            {
                "data": {
                    "score": "{:.1f}".format(assessment_response.risk_analysis.score),
                    "verdict": verdict,
                }
            }
        )
    except ValueError or Exception as e:
        return jsonify({"data": {"error_msg": str(e.__dict__)}})


# Return comment template.
def comment() -> str:
    return render_template(template_name_or_list="comment.html", context=context)


# On comment submit, execute reCAPTCHA Enterprise assessment and take action according to the score.
def on_comment_submit() -> Response:
    try:
        recaptcha_action = config["recaptcha_actions"]["comment"]
        json_data = json.loads(request.data)

        # <!-- ATTENTION: reCAPTCHA Example (Server Part 1/2) Starts -->
        assessment_response = create_assessment(
            context.get("project_id"),
            context.get("site_key"),
            json_data["token"],
        )

        # Check if the token is valid, score is above threshold score and the action equals expected.
        if assessment_response.token_properties.valid and \
                assessment_response.risk_analysis.score > SAMPLE_THRESHOLD_SCORE and \
                assessment_response.token_properties.action == recaptcha_action:
            # Check if comment has safe language and proceed to store in database.
            # comment = json_data["comment"]
            # Business logic.
            # Classify the action as not bad.
            verdict = "Not Bad"
        else:
            # If any of the above condition fails, trigger email/phone verification flow.
            # Classify the action as bad.
            verdict = "Bad"
        # <!-- ATTENTION: reCAPTCHA Example (Server Part 1/2) Ends -->

        # Return the risk score.
        return jsonify(
            {
                "data": {
                    "score": "{:.1f}".format(assessment_response.risk_analysis.score),
                    "verdict": verdict,
                }
            }
        )
    except ValueError or Exception as e:
        return jsonify({"data": {"error_msg": str(e.__dict__)}})
