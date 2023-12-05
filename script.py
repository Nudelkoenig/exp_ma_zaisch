
import alfred3 as al
import alfred3_interact as ali
from thesmuggler import smuggle
import random
import numpy as np
import statistics
from matplotlib.figure import Figure

# External Sources

content = smuggle("files/content.py")
informed_consent = smuggle("files/informed_consent.py")
registration = smuggle("files/exp_registration.py")
screening = smuggle("files/exp_screening.py")

exp = al.Experiment()


class MatchingTimeoutPage(al.Page):
    title = "Wartezeit überschritten"

    def on_exp_access(self):
        self += al.VerticalSpace("50px")
        self += al.Text(text="Wartezeit überschritten",
            align="center",
        )


class WaitingTimeoutPage(al.Page):
    title = "Wartezeit überschritten"
    name = "waiting_timeout"

    def on_exp_access(self):
        self += al.VerticalSpace("50px")
        self += al.Text(text="Wartezeit überschritten",
            align="center",
        )


class WaitingExceptionPage(al.Page):
    title = "Experiment abgebrochen"
    name = "waiting_exception"

    def on_exp_access(self):
        self += al.VerticalSpace("50px")
        self += al.Text(text="Experiment abgebrochen",
            align="center",
        )


class Match(ali.WaitingPage):
    title = "Bitte habe noch einen Moment Geduld"
    name = "matching_page"
    wait_msg = "Waiting for match"

    wait_timeout = 10 * 60

    def wait_for(self):
        timeout_page = al.Page(title="Experimentaufbau fehlgeschlagen",
                               name="nomatch_page")
        timeout_page += al.Text(text="Experimentaufbau fehlgeschlagen")

        self.wait_timeout_page = MatchingTimeoutPage(name="waiting_timeout")
        self.wait_exception_page = WaitingExceptionPage()

        mm = self.exp.plugins.mm

        # match to group

        group = mm.match_random(nmin=2, wait=60)
        self.exp.plugins.group = group

        # determine condition
        self.exp.condition = group.spec_name

        return True


@exp.setup
def setup(exp):

    roles = ["judge", "advisor"]
    block_blind = ali.ParallelSpec(*roles, nslots=126, name="block_blind")
    block_feedback = ali.ParallelSpec(*roles, nslots=126, name="block_feedback")
    sequential_blind = ali.ParallelSpec(*roles, nslots=126, name="sequential_blind")
    sequential_feedback = ali.ParallelSpec(*roles, nslots=126, name="sequential_feedback")
    exp.plugins.mm = ali.MatchMaker(block_blind, block_feedback, sequential_blind, sequential_feedback, exp=exp)


class InstructionPagePhase1(al.Page):
    name = "instr_phase_1"
    title = content.instr_phase_1_title

    def on_first_show(self):
        group = self.exp.plugins.group
        role = group.me.role
        if self.exp.condition == "block_feedback" and role == "judge":
            self += al.Text(
                name="instr_phase_1_judge_block_aware", text=content.phase_one_instruction_judge_block_aware
            )
            self += al.Image(
                path=self.exp.path/"files/judge_block_aware.png",
                position="center",
                name=f"image_judge_block_aware",
                align="left",
                width="full",
            )
            self += al.Text(
                name="instr_phase_1_greeting", text=content.phase_one_instruction_greeting
            )
        elif self.exp.condition == "block_feedback" and role == "advisor":
            self += al.Text(
                name="instr_phase_1_advisor_block_aware", text=content.phase_one_instruction_advisor_block_aware
            )
            self += al.Image(
                path=self.exp.path/"files/adv_block_aware.png",
                position="center",
                name=f"image_advisor_block_aware",
                align="left",
                width="full",
            )
            self += al.Text(
                name="instr_phase_1_greeting", text=content.phase_one_instruction_greeting
            )
        elif self.exp.condition == "block_blind" and role == "judge":
            self += al.Text(
                name="instr_phase_1_judge_block_unaware", text=content.phase_one_instruction_judge_block_unaware
            )
            self += al.Image(
                path=self.exp.path/"files/judge_block_unaware.png",
                position="center",
                name=f"image_judge_block_unaware",
                align="left",
                width="full",
            )
            self += al.Text(
                name="instr_phase_1_greeting", text=content.phase_one_instruction_greeting
            )
        elif self.exp.condition == "block_blind" and role == "advisor":
            self += al.Text(
                name="instr_phase_1_advisor_block_unaware", text=content.phase_one_instruction_advisor_block_unaware
            )
            self += al.Image(
                path=self.exp.path/"files/adv_block_unaware.png",
                position="center",
                name=f"image_advisor_block_unaware",
                align="left",
                width="full",
            )
            self += al.Text(
                name="instr_phase_1_greeting", text=content.phase_one_instruction_greeting
            )
        elif self.exp.condition == "sequential_feedback" and role == "judge":
            self += al.Text(
                name="instr_phase_1_judge_sequence_aware", text=content.phase_one_instruction_judge_sequence_aware
            )
            self += al.Image(
                path=self.exp.path/"files/judge_sequence_aware.png",
                position="center",
                name=f"image_judge_sequence_aware",
                align="left",
                width="full",
            )
            self += al.Text(
                name="instr_phase_1_greeting", text=content.phase_one_instruction_greeting
            )
        elif self.exp.condition == "sequential_feedback" and role == "advisor":
            self += al.Text(
                name="instr_phase_1_advisor_sequence_aware", text=content.phase_one_instruction_advisor_sequence_aware
            )
            self += al.Image(
                path=self.exp.path/"files/adv_sequence_aware.png",
                position="center",
                name=f"image_advisor_sequence_aware",
                align="left",
                width="full",
            )
            self += al.Text(
                name="instr_phase_1_greeting", text=content.phase_one_instruction_greeting
            )
        elif self.exp.condition == "sequential_blind" and role == "judge":
            self += al.Text(
                name="instr_phase_1_judge_sequence_unaware", text=content.phase_one_instruction_judge_sequence_unaware
            )
            self += al.Image(
                path=self.exp.path/"files/judge_sequence_unaware.png",
                position="center",
                name=f"image_judge_sequence_unaware",
                align="left",
                width="full",
            )
            self += al.Text(
                name="instr_phase_1_greeting", text=content.phase_one_instruction_greeting
            )
        elif self.exp.condition == "sequential_blind" and role == "advisor":
            self += al.Text(
                name="instr_phase_1_advisor_sequence_unaware", text=content.phase_one_instruction_advisor_sequence_unaware
            )
            self += al.Image(
                path=self.exp.path/"files/adv_sequence_unaware.png",
                position="center",
                name=f"image_advisor_sequence_unaware",
                align="left",
                width="full",
            )
            self += al.Text(
                name="instr_phase_1_greeting", text=content.phase_one_instruction_greeting
            )


class InstructionCheckPage(al.Page):
    def on_first_show(self):
        group = self.exp.plugins.group
        role = group.me.role

        self += al.Text("Im Folgenden haben wir einige Fragen an dich bezüglich des Experiments an dem du gleich"
                        " arbeiten wirst.", align="center", width="wide")

        self += al.Hline()

        self += al.Text("Was ist deine Aufgabe bei der folgenden Studie?", align="center", width="wide")

        self += al.SingleChoiceButtons("Allgemeinwissensfragen beantworten",
                                       "Flusslängen schätzen",
                                       "Kaloriengehalt von Lebensmittel schätzen",
                                       name=f'instruction_check_1',
                                       align="center",
                                       font_size="normal",
                                       width="wide",
                                       force_input=True,
                                       description=f'Instruction check 1 '
                                                   f'(What is your task in this experiment)'
                                       )

        self += al.Hline()

        self += al.Text("Welche Informationen werden mit deinem:r Partner:in geteilt?", align="center", width="wide")

        self += al.SingleChoiceButtons("Meine Schätzungen",
                                       "Meine Sicherheit bei meinen Schätzungen",
                                       "gar keine Informationen über meine Schätzungen",
                                       name=f'instruction_check_2',
                                       align="center",
                                       font_size="normal",
                                       width="wide",
                                       force_input=True,
                                       description=f'Instruction check 2 '
                                                   f'(Which Information does your partner see?)'
                                       )

        self += al.Hline()

        self += al.Text("Mit wem arbeitest du zusammen?", align="center", width="wide")

        self += al.SingleChoiceButtons("Mit allen Personen in diesem Raum",
                                       "Wechselnd, immer mit einer anderen Person",
                                       "mit einer festen Person hier im Raum",
                                       name=f'instruction_check_3',
                                       align="center",
                                       font_size="normal",
                                       width="wide",
                                       force_input=True,
                                       description=f'Instruction check 3'
                                                   f'(Who are you going to work with?)'
                                       )

        self += al.Hline()

        self += al.Text("Was sind die Ratschläge?", align="center", width="wide")

        self += al.SingleChoiceButtons("Meine Schätzungen, die meinem:r Partner:in übermittelt werden",
                                       "Die Schätzungen meines:r Partner:in, die ich erhalten",
                                       "Die Schätzungen von Personen die bereits früher an der Studie "
                                       "teilgenommen haben",
                                       name=f'instruction_check_4',
                                       align="center",
                                       font_size="normal",
                                       width="wide",
                                       force_input=True,
                                       description=f'Instruction check 4'
                                                   f'(What is the advice?)'
                                       )

        if role == "judge":
            self += al.Hline()

            self += al.Text("Wann macht der:die Ratgeber:in die Schätzungen, die als Ratschläge übermittelt werden?",
                            align="center", width="wide")

            self += al.SingleChoiceButtons("Die Ratschläge stammen von einer Person, die in einer vergangenen Sitzung "
                                           "an dem Experiment teilgenommen hat",
                                           "Der:die Ratgeber:in gibt alle Ratschläge ab, bevor ich mit meinen Schätzungen "
                                           "beginne",
                                           "Der:die Ratgeber:in gibt bei jeder Aufgabe, parallel mit meiner ersten Schätzung, "
                                           "seinen Ratschlag ab",
                                           name=f'instruction_check_5',
                                           align="center",
                                           font_size="normal",
                                           width="wide",
                                           force_input=True,
                                           description=f'Instruction check 5'
                                                       f'(Can the advisor react?)'
                                           )
        else:
            self += al.Hline()

            self += al.Text("Kannst du sehen, was dein:e Partner:in anhand deines Ratschlags für eine finale "
                            "Schätzung trifft?",
                            align="center", width="wide")

            self += al.SingleChoiceButtons(
                "Nein, bei keiner Aufgabe",
                "Ja, bei manchen Aufgaben",
                "Ja, bei jeder Aufgabe",
                name=f'instruction_check_6',
                align="center",
                font_size="normal",
                width="wide",
                force_input=True,
                description=f'Instruction check 6'
                            f'(Can you see the final estimate of the judge?)'
                )

    def custom_move(self):
        group = self.exp.plugins.group
        role = group.me.role
        if self.exp.condition == "sequential_feedback":
            if role == "judge":
                if self.data.get("instruction_check_1")["value"] == 1 and self.data.get("instruction_check_2")["value"]== 1 and self.data.get("instruction_check_3")["value"] == 3 and self.data.get("instruction_check_4")["value"] == 2 and self.data.get("instruction_check_5")["value"] == 3:
                    self.exp.jump(to="instruction_check_success")
                else:
                    return True
            elif role == "advisor":
                if self.data.get("instruction_check_1")["value"] == 1 and self.data.get("instruction_check_2")["value"] == 1 and self.data.get("instruction_check_3")["value"] == 3 and self.data.get("instruction_check_4")["value"] == 1 and self.data.get("instruction_check_6")["value"] == 3:
                    self.exp.jump(to="instruction_check_success")
                else:
                    return True
        if self.exp.condition == "sequential_blind":
            if role == "judge":
                if self.data.get("instruction_check_1")["value"] == 1 and self.data.get("instruction_check_2")["value"] == 3 and self.data.get("instruction_check_3")["value"] == 3 and self.data.get("instruction_check_4")["value"] == 2 and self.data.get("instruction_check_5")["value"] == 3:
                    self.exp.jump(to="instruction_check_success")
                else:
                    return True
            elif role == "advisor":
                if self.data.get("instruction_check_1")["value"] == 1 and self.data.get("instruction_check_2")["value"] == 1 and self.data.get("instruction_check_3")["value"] == 3 and self.data.get("instruction_check_4")["value"] == 1 and self.data.get("instruction_check_6")["value"] == 1:
                    self.exp.jump(to="instruction_check_success")
                else:
                    return True
        if self.exp.condition == "block_feedback":
            if role == "judge":
                if self.data.get("instruction_check_1")["value"] == 1 and self.data.get("instruction_check_2")["value"] == 1 and self.data.get("instruction_check_3")["value"] == 3 and self.data.get("instruction_check_4")["value"] == 2 and self.data.get("instruction_check_5")["value"] == 2:
                    self.exp.jump(to="instruction_check_success")
                else:
                    return True
            elif role == "advisor":
                if self.data.get("instruction_check_1")["value"] == 1 and self.data.get("instruction_check_2")["value"] == 1 and self.data.get("instruction_check_3")["value"] == 3 and self.data.get("instruction_check_4")["value"] == 1 and self.data.get("instruction_check_6")["value"] == 3:
                    self.exp.jump(to="instruction_check_success")
                else:
                    return True
        if self.exp.condition == "block_blind":
            if role == "judge":
                if self.data.get("instruction_check_1")["value"] == 1 and self.data.get("instruction_check_2")["value"] == 3 and self.data.get("instruction_check_3")["value"] == 3 and self.data.get("instruction_check_4")["value"] == 2 and self.data.get("instruction_check_5")["value"] == 2:
                    self.exp.jump(to="instruction_check_success")
                else:
                    return True
            elif role == "advisor":
                if self.data.get("instruction_check_1")["value"] == 1 and self.data.get("instruction_check_2")["value"] == 1 and self.data.get("instruction_check_3")["value"] == 3 and self.data.get("instruction_check_4")["value"] == 1 and self.data.get("instruction_check_6")["value"] == 1:
                    self.exp.jump(to="instruction_check_success")
                else:
                    return True

# [JR] Right here I need to add a check whether participants passed the instruction check based on which
# condition and role they were assigned to.

# [JR] Then I need to implement a custom move that moves participants forward to the task if they passed the instruction
# check or moves them to an additional page that tells them they answered at least one question wrong and then moves
# them back to the instruction page.


class InstructionCheckFailPage(al.Page):
    name = "instruction_check_fail"

    def on_exp_access(self):
        self += al.Text(f"Du hast leider eine oder mehrere der Fragen zum Verständnis der Instruktionen falsch "
                        f"beantwortet. <br> <br> Klick auf 'weiter' und lies dir die Instruktionen nochmals gründlich"
                        f" durch", align="center", width="wide")

    def custom_move(self):
        self.exp.jump(to="instr_phase_1")
# [JR] Here I need another custom move back to the instruction page


class InstructionCheckSuccessPage(al.Page):
    name = "instruction_check_success"

    def on_first_show(self):
        self += al.Text(f"Du hast alle Fragen zum Verständnis der Instruktionen richtig beantwortet."
                        f"<br> <br> Klick auf 'weiter' um mit der Bearbeitung der Schätzaufgaben zu beginnen.",
                        align="center", width="wide")


class InstructionPagePhase2(al.Page):
    name = "instr_phase_2"
    title = "Instruktionen Teil 2"

    def on_first_show(self):
        group = self.exp.plugins.group
        role = group.me.role
        if self.exp.condition == "block_feedback" and role == "judge":
            self += al.Text(
                name="instr_phase_2_judge_block", text=content.phase_two_instruction_judge_block
            )

        elif self.exp.condition == "block_blind" and role == "judge":
            self += al.Text(
                name="instr_phase_2_judge_block", text=content.phase_two_instruction_judge_block
            )

        elif self.exp.condition == "block_feedback" and role == "advisor":
            self += al.Text(
                name="instr_phase_2_advisor_block_aware", text=content.phase_two_instruction_advisor_block_aware
            )


class InstructionPagePhase3(al.Page):
    name = "instr_phase_3"
    title = "Ende der Schätzaufgaben"

    def on_first_show(self):
        self += al.Text(
                name="instr_phase_final_question", text=content.final_questionnaire_instruction
        )


class PhaseOneInitialEstimate(al.Page):
    def on_first_show(self):

        data = self.vargs.taskdata
        i = self.vargs.i
        suffix = self.vargs.get("suffix", "")
        stimulus = data["stimulus"]
        description = data["label"]
        unit = data["unit"]
        true_value = data["true_value"]

        self += al.Text(
            text=f"<b><u>{description}</u></b>",
            font_size=16,
            name=f"description_{i:02}" + suffix,
            position="left",
            align="center",
        )

        self += al.Hline()

        self += al.NumberEntry(
            ndecimals=0,
            name=f"estimation_trial_{i:02}" + suffix,
            width="wide",
            force_input=True,
            suffix=f"{unit}",
            align="center",
            min=0,

        )

        self += al.Value(
            value=stimulus,
            name=f'trial_{i:02d}_stimulus',
            description=f"stimulus used in"
                        f"trial {i:02d}"
        )

        self += al.Hline()

        self += al.Text(
                "Bitte gib an, wie sicher du dir deiner Schätzung bist ",
                align="center",
                width="wide"
            )

        self += al.SingleChoiceButtons(
                "sehr unsicher",
                "unsicher",
                "eher unsicher",
                "weder noch",
                "eher sicher",
                "sicher",
                "sehr sicher",
                name=f'trial_{i:02}_initial_confidence',
                align="center",
                font_size="normal",
                width="wide",
                force_input=True,
                description=f'Initial confidence rating for trial {i:02} '
                            f'(Bitte gib an, wie sicher du dir deiner Schätzung bist)'

            )

        self += al.Value(true_value, name=f"true_value_{i}")


class SyncPage(ali.WaitingPage):
    def wait_for(self):
        g = self.exp.plugins.group
        i = self.vargs.i
        suffix = self.vargs.get("suffix", "")

        estimates = [m.values.get(f"estimation_trial_{i:02}" + suffix) for m in g.members()]
        return all(estimates)


class SyncPage2(ali.WaitingPage):
    def wait_for(self):
        judge = self.exp.plugins.group.judge
        data = self.vargs.taskdata
        i = self.vargs.i

        estimates = [judge.values.get(f'trial_{i:02d}_final_estimate')]
        return all(estimates)


class SyncPageBlock(ali.WaitingPage):
    def wait_for(self):
        advisor = self.exp.plugins.group.advisor

        return advisor.values.get(f"estimation_trial_{20:02}", False)


class PhaseTwoFinalEstimate(al.Page):
    def on_first_show(self):

        g = self.exp.plugins.group
        role = g.me.role
        advisor = self.exp.plugins.group.advisor
        data = self.vargs.taskdata
        i = self.vargs.i
        suffix = self.vargs.get("suffix", "")
        description = data["label"]
        unit = data["unit"]

        if role == "judge":
            advice = round(advisor.values.get(f"estimation_trial_{i:02}" + suffix))

            self += al.Text(
                text=f"<b><u>{description}</u></b>",
                font_size=16,
                name=f"description_{i:02}_phase2" + suffix,
                position="center",
                align="center",
            )

            self += al.Value(
                value=advice,
                name=f'trial_{i:03d}_adv_values',
                description=f"Python list of all estimates used for advice in "
                            f"trial {i:02d}"
            )

            self += al.Text(
                f"Deine erste Schätzung:<b> "
                f"{round(self.exp.values[f'estimation_trial_{i:02}' + suffix])} {unit}"
                f"</b>",
                align="center"
            )

            self += al.Hline()

            adv_text = "<b>die Schätzung</b> deines:er " \
                       "Ratgeber:in"

            self += al.Text(
                f"Du erhältst nun als Ratschlag {adv_text}:<br><br><b>"
                f"{advice} {unit}</b><br>",
                align="center",
                width="wide"
            )

            self += al.Hline()

            self += al.Text(
                "Bitte gib nun deine finale Schätzung ab",
                align="center",
                width="wide"
            )

            self += al.NumberEntry(
                name=f'trial_{i:02d}_final_estimate' + suffix,
                ndecimals=0,
                min=0,
                leftlab=al.Label("Deine finale Schätzung:", align="right"),
                align="center",
                width="wide",
                layout=(5, 4),
                force_input=True,
                suffix=f"{unit}",
                description=f'Final calorie estimate (after receiving advice) in '
                            f'trial {i:03d} (Bitte geben Sie nun Ihre finale '
                            f'Schätzung der Kalorienzahl ab)'
            )

            self += al.Hline()

            self += al.Text(
                "Bitte gib an, wie sicher du dir deiner Schätzung bist ",
                align="center",
                width="wide"
            )

            self += al.SingleChoiceButtons(
                "sehr unsicher",
                "unsicher",
                "eher unsicher",
                "weder noch",
                "eher sicher",
                "sicher",
                "sehr sicher",
                name=f'trial_{i:02d}_final_confidence',
                align="center",
                font_size="normal",
                width="wide",
                force_input=True,
                description=f'Final confidence rating in trial {i:02d} '
                            f'(GBitte gib an, wie sicher du dir deiner Schätzung bist )'
            )

        else:
            pass


class FeedbackPage(al.Page):
    def on_first_show(self):

        g = self.exp.plugins.group
        role = g.me.role
        judge = self.exp.plugins.group.judge
        advisor = self.exp.plugins.group.advisor
        data = self.vargs.taskdata
        i = self.vargs.i
        suffix = self.vargs.get("suffix", "")
        description = data["label"]
        unit = data["unit"]

        if role == "judge":
            pass
        else:
            advice = advisor.values.get(f"estimation_trial_{i:02}" + suffix)
            final_estimate = judge.values.get(f'trial_{i:02d}_final_estimate')
            initial_estimate = judge.values.get(f"estimation_trial_{i:02}" + suffix)

            self += al.Text(
                text=f"<b><u>{description}</u></b>",
                font_size=16,
                name=f"description_{i:02}_phase2" + suffix,
                position="center",
                align="center",
            )
            self += al.Text(
                f"Die erste Schätzung deines:r Partner:in:<b> "
                f"{round(initial_estimate)} {unit}"
                f"</b>",
                align="center"
            )

            self += al.Text(
                f"Dein Ratschlag:<b> "
                f"{round(advice)} {unit}"
                f"</b>",
                align="center"
            )

            self += al.Text(
                f"Die finale Schätzung deines:r Partner:in:<b> "
                f"{round(final_estimate)} {unit}"
                f"</b>",
                align="center"
            )


class JudgeAccuracyPage(al.Page):
    title = "Wahrnehmung der Schätzungen"
    name = "judge_accuracy_page"

    def on_first_show(self):

        self += al.Text(
            "Bitte denk noch einmal über deine eben abgegebenen Schätzungen und die von deinem:r Partner:in erhaltenen "
            "Ratschläge nach. Beantworte dazu bitte folgende Fragen. Akkuratheit bedeutet hier, dass die Schätzungen "
            "sehr nah an den wahren Werten sind. Ungenaue Schätzungen sind also nicht besonders akkurat.",
            align="center",
            width="wide"
        )

        self += al.Hline()

        self += al.Text(content.initial_own_accuracy,
            align="center",
            width="wide")

        self += al.SingleChoiceButtons(
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            leftlab="überhaupt nicht akkurat",
            rightlab="sehr akkurat",
            name="initial_own_accuracy",
            align="center",
            font_size="normal",
            width="wide",
            force_input=True,
            description=f'Subjective initial accuracy'
        )

        self += al.Hline()

        self += al.Text(content.final_own_accuracy,
                        align="center",
                        width="wide")

        self += al.SingleChoiceButtons(
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            leftlab="überhaupt nicht akkurat",
            rightlab="sehr akkurat",
            name="final_own_accuracy",
            align="center",
            font_size="normal",
            width="wide",
            force_input=True,
            description=f'Subjective final accuracy'
        )

        self += al.Hline()

        self += al.Text(content.absolut_advice_accuracy,
                        align="center",
                        width="wide")

        self += al.SingleChoiceButtons(
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            leftlab="überhaupt nicht akkurat",
            rightlab="sehr akkurat",
            name="absolut_advice_accuracy",
            align="center",
            font_size="normal",
            width="wide",
            force_input=True,
            description=f'Subjective advice accuracy'
        )
        self += al.Hline()

        self += al.Text(content.relative_advice_accuracy,
                        align="center",
                        width="wide")

        self += al.SingleChoiceButtons(
            "-3",
            "-2",
            "-1",
            "0",
            "1",
            "2",
            "3",
            leftlab="viel weniger akkurat",
            rightlab="viel akkurater",
            name="relative_advice_accuracy",
            align="center",
            font_size="normal",
            width="wide",
            force_input=True,
            description=f'Relative advice accuracy'
        )


class JudgeFairnessPage(al.Page):
    title = "Fokus bei der zweiten Schätzung"
    name = "judge_fairness_page"

    def on_first_show(self):

        self += al.Text(
            "Bitte denk an diejenigen Durchgänge, in denen du den Ratschlag deines:r Partner:in berücksichtigt "
            "hast. Uns interessiert nun, aus welchem Grund du die Ratschläge berücksichtigt hast. "
            "<br><br>",
            align="center",
            width="wide"
        )
        self += al.Text(
            "Der Einfachheit "
            "halber gehen wir bei dieser Frage davon aus, dass es zwei mögliche Gründe gibt. Erstens wegen des "
            "<b>Informationsgehalts</b> der Ratschläge, d.h. du hast die Ratschläge deshalb berücksichtigt, weil du"
            " eine möglichst gute zweite Schätzung abgeben wolltest. Zweitens aus Gründen der <b>Fairness</b>, d.h. du "
            "hast die Ratschläge deshalb berücksichtigt, weil es gegenüber deiner:m Partner:in unfair gewesen wäre, "
            "die Ratschläge zu ignorieren. <br>"
            "Bitte gib im Hinblick auf diese beiden möglichen Gründe an, weshalb du die Ratschläge"
            " berücksichtigt hast. Ein Wert von -5 bedeutet dabei, dass du die Ratschläge ausschließlich "
            "genutzt hast, um dadurch bessere Schätzungen abzugeben. Ein Wert von +5 besagt, dass du die Ratschläge "
            "nur aus Gründen der Fairness berücksichtigt hast. Werte zwischen -5 und +5 bilden ab, dass beide Gründe "
            "für dich eine Rolle gespielt haben. Ein Wert von 0 bedeutet dabei, dass beide Gründe in gleichem Ausmaß"
            " zutreffen.",
            align="center",
            width="wide")

        self += al.SingleChoiceButtons(
            "-5",
            "-4",
            "-3",
            "-2",
            "-1",
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            leftlab="Ausschließlich auf Grund des Informationsgehalt",
            rightlab="Ausschließlich aus Fairness gegenüber Partner:in",
            bottomlab="Informationsgehalt und Fairness gleichermaßen",
            name="focus_judge",
            align="center",
            font_size="normal",
            width="wide",
            force_input=True,
            description=f'Reasoning behind following advice'
                        f'(Warum wurden die Ratschläge berücksichtigt? Fairness oder Akkuratheit )'
        )


class JudgeFairnessPage2(al.Page):
    title = "Weitere Fragen zu der zweiten Schätzung"
    name = "judge_fairness_page2"

    def on_first_show(self):

        self += al.Text(
            "Nun wollen wir es noch einmal etwas genauer wissen. Wir haben hier eine Reihe von verschiedenen "
            "Motivationen aufgeschrieben, die unterschiedlich wichtige Rollen für die Berücksichtigung der Ratschläge "
            "spielen können. Bitte gib auf dieser Seite an, wie wichtig die verschiedenen Gründe in den Durchgängen, "
            "in denen du den Ratschlag deines:r Partner:in berücksichtigt hast, für dich waren. Am Ende der Seite hast "
            "du zusätzlich die Möglichkeit weitere Gründe für die Berücksichtigung der Ratschläge anzugeben.",
            align="center",
            width="wide"
        )

        self += al.Hline()

        self += al.Text(
            "Wie wichtig war es dir, deinem:r Partner:in gegenüber fair zu sein?",
            align="center",
            width="wide")

        self += al.SingleChoiceButtons(
            "1 <br> gar nicht wichtig",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7 <br> sehr wichtig",
            name="fairness_judge",
            align="center",
            font_size="normal",
            width="wide",
            force_input=True,
            description=f'Importance of fairness'
                        f'(Wie wichtig war es dir, deinem:r Partner:in gegenüber fair zu sein?)'
        )

        self += al.Hline()

        self += al.Text(
            "Wie wichtig war es dir, eine möglichst genaue endgültige Schätzung abzugeben?",
            align="center",
            width="wide")

        self += al.SingleChoiceButtons(
            "1 <br> gar nicht wichtig",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7 <br> sehr wichtig",
            name="accuracy_judge",
            align="center",
            font_size="normal",
            width="wide",
            force_input=True,
            description=f'Importance of accuracy'
                        f'(Wie wichtig war es dir, eine möglichst genaue endgültige Schätzung abzugeben?)'
        )

        self += al.Hline()

        self += al.Text(
            "Wie wichtig war es dir, dass dein:e Partner:in sich wertgeschätzt fühlt?",
            align="center",
            width="wide")

        self += al.SingleChoiceButtons(
            "1 <br> gar nicht wichtig",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7 <br> sehr wichtig",
            name="appreciation_judge",
            align="center",
            font_size="normal",
            width="wide",
            force_input=True,
            description=f'Importance of showing appreciation'
                        f'(Wie wichtig war es dir, dass dein:e Partner:in sich wertgeschätzt fühlt?)'
        )

        self += al.Hline()

        self += al.Text(
            "Wie wichtig war es dir, bei der endgültigen Schätzung besser zu werden als bei der ersten Schätzung?",
            align="center",
            width="wide")

        self += al.SingleChoiceButtons(
            "1 <br> gar nicht wichtig",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7 <br> sehr wichtig",
            name="improvement_judge",
            align="center",
            font_size="normal",
            width="wide",
            force_input=True,
            description=f'Importance of improving in the second judgement'
                        f'(Wie wichtig war es dir, bei der endgültigen Schätzung besser zu werden als bei der '
                        f'ersten Schätzung?)'
        )

        self += al.Hline()
        self += al.Text(
            "Gab es andere Gründe, aus denen du die Ratschläge deines:r Partner:in berücksichtigt hast? Dann schreib "
            "sie bitte hier auf.",
            align="center",
            width="wide")
        self += al.TextArea(
            name='other_reasons',
            width='wide',
            nrows=15,
            force_input=False,
            bottomlab=al.Label('Hinweis: Das Textfeld kann bei Bedarf an der rechten unteren Ecke vergrößert werden.',
                               font_size='small')
        )


class JudgeManiCheckPage(al.Page):
    title = "Bearbeitung der Schätzaufgaben"
    name = "judge_mani_check_page"

    def on_first_show(self):
        group = self.exp.plugins.group

        self += al.Text(content.seriousness_mani_check,
                        align="center",
                        width="wide")

        self += al.SingleChoiceButtons(
            "ja",
            "nein",
            name="seriousness_mani_check",
            align="center",
            font_size="normal",
            width="wide",
            force_input=True,
            description=f'Did you work seriously'
        )

        self += al.Hline()

        self += al.Text(content.awareness_mani_check,
                        align="center",
                        width="wide")

        self += al.SingleChoiceButtons(
            "ja",
            "nein",
            name="awareness_mani_check",
            align="center",
            font_size="normal",
            width="wide",
            force_input=True,
            description=f'Was your advisor able to see how you used his advice?'
        )


class AdvisorFairnessPage1(al.Page):
    def on_first_show(self):
        self += al.Text(
            "Im Folgenden werden wir dir einige Fragen nach der Zusammenarbeit mit deinem:r Partner:in stellen",
            align="center",
            width="wide"
        )

        self += al.Hline()

        self += al.Text(
            "Als wie fair bewertest du die Zusammenarbeit mit deinem:r Partner:in insgesamt? ",
            width="wide"
        )

        self += al.SingleChoiceButtons(
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            leftlab="Überhaupt nicht fair",
            rightlab="Sehr fair",
            name="general_fairness_advisor",
            align="center",
            font_size="normal",
            width="wide",
            force_input=True,
            description=f'How fair was the work with your partner'
        )
        self += al.Hline()

        self += al.Text(
            "Wie motiviert bist du mit dem:r Partner:in, mit dem:der du die letzten 20 Aufgaben bearbeitet hast, noch "
            " weitere Schätzaufgaben zu bearbeiten?",
            align="center",
            width="wide"
        )

        self += al.SingleChoiceButtons(
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            leftlab="überhaupt nicht motiviert",
            rightlab="sehr motiviert",
            name="motivation_advisor",
            align="center",
            font_size="normal",
            width="wide",
            force_input=True,
            description=f'Advisor motivation to continue working with judge'
        )

        self += al.Hline()

        self += al.Text(
            "Würdest du für weitere Schätzaufgaben lieber mit der:m Partner:in, mit der:m du bisher "
            "zusammengearbeitet hast, oder mit einer:m anderen Partner:in weiterarbeiten?",
            align="center",
            width="wide"
        )

        self += al.SingleChoiceBar(
            "Weiter mit der:m <b>bisherigen</b> Partner:in",
            "Weiter mit einer:m <b>anderen</b> Partner:in",
            name="new_teammate_advisor",
            align="center",
            font_size="normal",
            width="wide",
            force_input=True,
            description=f'Advisor decision to continue working with old or new judge'
        )

        self += al.Hline()

        self += al.Text(
            "Wie stark ist dein Wunsch bei weiteren Aufgaben mit deiner:m bisherigen Partner:in bzw. mit "
            "einer:m anderen Partner:in zusammenzuarbeiten?",
            width="wide"
        )

        self += al.SingleChoiceButtons(
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            leftlab="Unbedingt eine:n neue:n Partner:in",
            rightlab="Unbedingt den:die bisherige:n Parter:in behalten",
            name="wish_for_change_advisor",
            align="center",
            font_size="normal",
            width="wide",
            force_input=True,
            description=f'How important is the decision to change/keep judge'
        )


class AdvisorManiCheckPage(al.Page):
    title = "Bearbeitung der Schätzaufgaben"
    name = "advisor_mani_check_page"

    def on_first_show(self):

        self += al.Text(content.seriousness_mani_check,
                        align="center",
                        width="wide")

        self += al.SingleChoiceButtons(
            "ja",
            "nein",
            name="seriousness_mani_check",
            align="center",
            font_size="normal",
            width="wide",
            force_input=True,
            description=f'Did you work seriously'
        )


# For this the goal will be to draw four random trials from the estimation task, basically resembling the FeedbackPage
# with the addition of the question how fair the advisor found that specific interaction/ trial to be.
class AdvisorFairnessPage2(al.Page):
    title = "Als wie fair empfindest du diesen konkreten Austausch mit deinem:r Partner:in?"

    def on_first_show(self):
        g = self.exp.plugins.group
        role = g.me.role
        judge = self.exp.plugins.group.judge
        advisor = self.exp.plugins.group.advisor
        data = self.vargs.taskdata
        i = self.vargs.i
        suffix = self.vargs.get("suffix", "")
        description = data["label"]
        unit = data["unit"]

        if role == "judge":
            pass
        else:
            advice = advisor.values.get(f"estimation_trial_{i:02}" + suffix)
            final_estimate = judge.values.get(f'trial_{i:02d}_final_estimate')
            initial_estimate = judge.values.get(f"estimation_trial_{i:02}" + suffix)

            self += al.Text(
                text=f"<b><u>{description}</u></b>",
                font_size=16,
                name=f"redescription_{i:02}_phase2" + suffix,
                position="center",
                align="center",
            )
            self += al.Text(
                f"Die erste Schätzung deines:r Partner:in:<b> "
                f"{round(initial_estimate)} {unit}"
                f"</b>",
                align="center"
            )

            self += al.Text(
                f"Dein Ratschlag:<b> "
                f"{round(advice)} {unit}"
                f"</b>",
                align="center"
            )

            self += al.Text(
                f"Die finale Schätzung deines:r Partners:in:<b> "
                f"{round(final_estimate)} {unit}"
                f"</b>",
                align="center"
            )

            self += al.Hline()

            self += al.Text("Findest du dein:e Partner:in hat sich hier fair verhalten?")

            self += al.SingleChoiceButtons(
                "1 <br> gar nicht fair",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7 <br> sehr fair",
                name=f"fairness_advisor{i:02}",
                align="center",
                font_size="normal",
                width="wide",
                force_input=True,
                description=f'Advisor perception of fairness in trial {i:02}'
            )


class Success(al.Page):
    title = "Experiment erstellt"
    name = "success_page"

    def on_first_show(self):
        group = self.exp.plugins.group
        role = group.me.role

        self += al.VerticalSpace("30px")
        self += al.Text(":balloon: :tada: :balloon:", align="center", font_size=70)
        self += al.VerticalSpace("20px")
        self += al.Text("Während des folgenden Experiments übernimmst du die Rolle des:der ", align="center")

        if role == "judge":
            self += al.Text(f"<b> Entscheidungsträger:in</b>", align="center")
        elif role == "advisor":
            self += al.Text(f"<b> Ratgeber:in </b>", align="center")


class InformedConsentPage(informed_consent.InformedConsent):
    content = content.informed_consent_content


class TaskGenerationPage(al.AutoForwardPage):
    title = "Experiment erstellt"
    name = "task_generation_page"

    def on_first_show(self):

        data = list(self.section.exp.read_csv_todict("files/quiz_questions.csv", delimiter=","))
        self.section.shuffle_data(data) # self = self.section
        self.section.add_task_phase(data)


exp += al.ForwardOnlySection(name="main")


@exp.member(of_section="main")
class InstructionSection(al.Section):
    allow_forward = True
    allow_backward = False
    allow_jumpfrom = False
    allow_jumpto = False


@exp.member(of_section="InstructionSection")
class LandingPage(al.Page):
    title = "Begrüßung"

    def on_exp_access(self):
        self += al.Text(content.welcome_instruction,
                        align="left")
        self += al.Alert(
            category="info",
            text="<i>Sobald du dich auf den beiden folgenden Seiten mit den Teilnahmebedingungen einverstanden erklärst"
                 " und mittels deiner E-Mailadresse registriert hast, kannst du mit dem Versuch beginnen.</i>",
        )


@exp.member(of_section="InstructionSection")
class InformedConsentPage(informed_consent.InformedConsent):
    content = content.informed_consent_content


@exp.member(of_section="InstructionSection")
class ScreeningPage(screening.ScreeningPage):
    content = content.screening_page_content
    register_on_hiding = False
    mortimer_url = "https://alfredo3.psych.bio.uni-goettingen.de/mortimer3"
    part_check_filter = {"exp_pretest_ma_zaisch": {"exp_id": "64d1f8bac10ec5caf3418b4d"},
                         }


@exp.member(of_section="main")
class MatchSection1(al.Section):
    allow_forward = True
    allow_backward = False
    allow_jumpfrom = False
    allow_jumpto = False

    def on_exp_access(self):
        self += Match(name="match")


@exp.member(of_section="main")
class PhaseOne(al.Section):
    allow_forward = True
    allow_backward = False
    allow_jumpfrom = True
    allow_jumpto = True

    def on_exp_access(self):
        self += Success(name="success")
        print(self.exp.condition)
        self += TaskGenerationPage(timeout=0)
    #def on_enter(self):
     #   data = list(self.exp.read_csv_todict("files/quiz_questions.csv", delimiter=","))
      #  self.shuffle_data(data) # self = self.section
       # self.add_task_phase(data)

    def shuffle_data(self, data: list):
        group = self.exp.plugins.group

        random.Random(group.group_id).shuffle(data)
        new_list = [i["stimulus"] for i in data]
        self.exp.adata["task_data_permutation"] = new_list

    def add_task_phase(self, data: list):
        group = self.exp.plugins.group
        # determine condition
        self.exp.condition = group.spec_name
        role = group.me.role

        self += InstructionPagePhase1()
        self += InstructionCheckPage(name="instruction_check_page")
        self += InstructionCheckFailPage()
        self += InstructionCheckSuccessPage()

        if self.exp.condition == "sequential_feedback":

            # The trial data is received from ExperimentSession to generate the c  0 0
            if role == "judge":
                for i in range(1, 21):
                    vargs_a = {"taskdata": data[i - 1], "i": i}
                    name_a = f"task_page_{i:02}"
                    title_a = f"Aufgabe {i}"
                    title_b = f"Zweite Schätzung Aufgabe {i}"
                    name_b = f"phase2_task_page_{i:02}"

                    self += PhaseOneInitialEstimate(name=name_a,
                        title=title_a,
                        vargs=vargs_a)
                    self += SyncPage(title=f"Warten auf deine:n Partner:in",
                                     wait_msg=f"Abrufen des Ratschlags für Aufgabe {i:02d}", name=f"sync_trial_{i:02d}",
                                     vargs=vargs_a)
                    self += PhaseTwoFinalEstimate(
                       name=name_b,
                       title=title_b,
                       vargs=vargs_a)
                    self += SyncPage2(title=f"Warten auf deine:n Partner:in",
                                      wait_msg=f"Senden deiner Antworten an deine:n Partner:in für Aufgabe {i:02d}",
                                      name=f"second_sync_trial_{i:02d}",
                                      vargs=vargs_a)
                self += InstructionPagePhase3(name="instructions_final_questionnaire")
                self += JudgeManiCheckPage(name="mani_check_final_questionnaire")
                self += JudgeAccuracyPage(name="judge_accuracy_page")
                self += JudgeFairnessPage(name="judge_fairness_page_01")
                self += JudgeFairnessPage2(name="judge_fairness_page_02")

            if role == "advisor":

                for i in range(1, 21):
                    vargs_a = {"taskdata": data[i - 1], "i": i}
                    name_a = f"task_page_{i:02}"
                    title_a = f"Aufgabe {i}"

                    self += PhaseOneInitialEstimate(name=name_a,
                        title=title_a,
                        vargs=vargs_a)
                    self += SyncPage(title=f"Warten auf deine:n Partner:in",
                                     wait_msg=f"Senden des Ratschlags an deine:n Partner:in für Aufgabe {i:02d}",
                                     name=f"sync_trial_{i:02d}",
                                     vargs=vargs_a)
                    self += SyncPage2(title=f"Warten auf deine:n Partner:in",
                                      wait_msg=f"Empfangen der Antworten deines:deiner Partner:in bei "
                                            f"Aufgabe {i:02d}",
                                      name=f"second_sync_trial_{i:02d}",
                                      vargs=vargs_a)
                    self += FeedbackPage(title=f"Antworten deiner:s Partner:in bei Aufgabe {i:02d}",
                                         name=f"phase2_feedback_trial_{i:02}",
                                         vargs=vargs_a)
                self += InstructionPagePhase3(name="instructions_final_questionnaire")
                self += AdvisorManiCheckPage(name="mani_check_final_questionnaire")
                self += AdvisorFairnessPage1(name="advisor_fairness_page_01")
                self += AdvisorFairnessPage2(name="advisor_fairness_page_task_05",
                                             vargs={"taskdata": data[5 - 1], "i": 5})
                self += AdvisorFairnessPage2(name="advisor_fairness_page_task_10",
                                             vargs={"taskdata": data[10 - 1], "i": 10})
                self += AdvisorFairnessPage2(name="advisor_fairness_page_task_15",
                                             vargs={"taskdata": data[15 - 1], "i": 15})
                self += AdvisorFairnessPage2(name="advisor_fairness_page_task_20",
                                             vargs={"taskdata": data[20 - 1], "i": 20})

        elif self.exp.condition == "sequential_blind":

            if role == "judge":
                for i in range(1, 21):
                    vargs_a = {"taskdata": data[i - 1], "i": i}
                    name_a = f"task_page_{i:02}"
                    title_a = f"Aufgabe {i}"
                    title_b = f"Zweite Schätzung Aufgabe {i}"
                    name_b = f"phase2_task_page_{i:02}"
                    self += PhaseOneInitialEstimate(name=name_a,
                                                    title=title_a,
                                                    vargs=vargs_a)
                    self += SyncPage(title=f"Warten auf deine:n Partner:in",
                                     wait_msg=f"Abrufen des Ratschlags für Aufgabe {i:02d}", name=f"sync_trial_{i:02d}",
                                     vargs=vargs_a)
                    self += PhaseTwoFinalEstimate(
                        name=name_b,
                        title=title_b,
                        vargs=vargs_a)
                self += InstructionPagePhase3(name="instructions_final_questionnaire")
                self += JudgeManiCheckPage(name="mani_check_final_questionnaire")
                self += JudgeAccuracyPage(name="judge_accuracy_page")
                self += JudgeFairnessPage(name="judge_fairness_page_01")
                self += JudgeFairnessPage2(name="judge_fairness_page_02")

            if role == "advisor":
                for i in range(1, 21):
                    vargs_a = {"taskdata": data[i - 1], "i": i}
                    name_a = f"task_page_{i:02}"
                    title_a = f"Aufgabe {i}"

                    self += PhaseOneInitialEstimate(name=name_a,
                                                    title=title_a,
                                                    vargs=vargs_a)
                    self += SyncPage(title=f"Warten auf deine:n Partner:in",
                                     wait_msg=f"Dein:e Partner:in gibt gerade ihre:seine zweite Schätzung für "
                                              f"Aufgabe {i:02d} ab.",
                                     name=f"sync_trial_{i:02d}",
                                     vargs=vargs_a)
                self += InstructionPagePhase3(name="instructions_final_questionnaire")
                self += AdvisorManiCheckPage(name="mani_check_final_questionnaire")
                self += AdvisorFairnessPage1(name="advisor_fairness_page_01")

        elif self.exp.condition == "block_blind":
            if role == "judge":
                self += InstructionPagePhase2(title="Bitte habe noch einen Augenblick Geduld!")
                vargs_sync = {"taskdata": data[19], "i": 20}
                self += SyncPageBlock(title=f"Warten auf deine:n Partner:in",
                                      wait_msg=f"Dein:e Partner:in gibt gerade ihre:seine Ratschläge ab.",
                                      name=f"block_wait", vargs=vargs_sync)
                for i in range(1, 21):
                    vargs_a = {"taskdata": data[i - 1], "i": i}
                    name_a = f"task_page_{i:02}"
                    title_a = f"Aufgabe {i}"
                    title_b = f"Zweite Schätzung Aufgabe {i}"
                    name_b = f"phase2_task_page_{i:02}"
                    self += PhaseOneInitialEstimate(name=name_a,
                                                    title=title_a,
                                                    vargs=vargs_a)
                    self += PhaseTwoFinalEstimate(
                        name=name_b,
                        title=title_b,
                        vargs=vargs_a)
                self += InstructionPagePhase3(name="instructions_final_questionnaire")
                self += JudgeManiCheckPage(name="mani_check_final_questionnaire")
                self += JudgeAccuracyPage(name="judge_accuracy_page")
                self += JudgeFairnessPage(name="judge_fairness_page_01")
                self += JudgeFairnessPage2(name="judge_fairness_page_02")

            elif role == "advisor":
                for i in range(1, 21):
                    vargs_a = {"taskdata": data[i - 1], "i": i}
                    name_a = f"task_page_{i:02}"
                    title_a = f"Aufgabe {i}"

                    self += PhaseOneInitialEstimate(name=name_a,
                                                    title=title_a,
                                                    vargs=vargs_a)
                self += InstructionPagePhase3(name="instructions_final_questionnaire")
                self += AdvisorManiCheckPage(name="mani_check_final_questionnaire")
                self += AdvisorFairnessPage1(name="advisor_fairness_page_01")

        elif self.exp.condition == "block_feedback":
            if role == "judge":
                self += InstructionPagePhase2(title="Bitte habe noch einen Augenblick Geduld!")
                vargs_sync = {"taskdata": data[19], "i": 20}
                self += SyncPageBlock(title=f"Warten auf deine:n Partner:in",
                                      wait_msg=f"Dein:e Partner:in gibt gerade ihre:seine Ratschläge ab.",
                                      name=f"block_wait",
                                      vargs=vargs_sync)
                for i in range(1, 21):
                    vargs_a = {"taskdata": data[i - 1], "i": i}
                    name_a = f"task_page_{i:02}"
                    title_a = f"Aufgabe {i}"
                    title_b = f"Zweite Schätzung Aufgabe {i}"
                    name_b = f"phase2_task_page_{i:02}"
                    self += PhaseOneInitialEstimate(name=name_a,
                                                    title=title_a,
                                                    vargs=vargs_a)
                    self += PhaseTwoFinalEstimate(
                        name=name_b,
                        title=title_b,
                        vargs=vargs_a)
#                    self += SyncPage2(title=f"Synchronisation Teil 2 Aufgabe {i:03d}",
#                                      name=f"second_sync_trial_{i:03d}",
#                                      vargs=vargs_a)
                self += InstructionPagePhase3(name="instructions_final_questionnaire")
                self += JudgeManiCheckPage(name="mani_check_final_questionnaire")
                self += JudgeAccuracyPage(name="judge_accuracy_page")
                self += JudgeFairnessPage(name="judge_fairness_page_01")
                self += JudgeFairnessPage2(name="judge_fairness_page_02")

            elif role == "advisor":
                for i in range(1, 21):
                    vargs_a = {"taskdata": data[i - 1], "i": i}
                    name_a = f"task_page_{i:02}"
                    title_a = f"Aufgabe {i}"

                    self += PhaseOneInitialEstimate(name=name_a,
                                                    title=title_a,
                                                    vargs=vargs_a)
                self += InstructionPagePhase2(title="Instruktionen Teil2")

                for i in range(1, 21):
                    vargs_a = {"taskdata": data[i - 1], "i": i}

                    self += SyncPage2(title=f"Warten auf deine:n Partner:in",
                                      wait_msg=f"Empfangen der Antworten deines:deiner Partner:in bei "
                                            f"Aufgabe {i:02d}",
                                      name=f"second_sync_trial_{i:02d}",
                                      vargs=vargs_a)
                    self += FeedbackPage(title=f"Antworten deiner:s Partner:in bei Aufgabe {i:02d}",
                                         name=f"phase2_feedback_trial_{i:02}",
                                         vargs=vargs_a)
                self += InstructionPagePhase3(name="instructions_final_questionnaire")
                self += AdvisorManiCheckPage(name="mani_check_final_questionnaire")
                self += AdvisorFairnessPage1(name="advisor_fairness_page_01")
                self += AdvisorFairnessPage2(name="advisor_fairness_page_task_05",
                                             vargs={"taskdata": data[5 - 1], "i": 5})
                self += AdvisorFairnessPage2(name="advisor_fairness_page_task_10",
                                             vargs={"taskdata": data[10 - 1], "i": 10})
                self += AdvisorFairnessPage2(name="advisor_fairness_page_task_15",
                                             vargs={"taskdata": data[15 - 1], "i": 15})
                self += AdvisorFairnessPage2(name="advisor_fairness_page_task_20",
                                             vargs={"taskdata": data[20 - 1], "i": 20})


@exp.member(of_section="main")
class FQSection(al.Section):
    allow_forward = True
    allow_backward = False
    allow_jumpfrom = False
    allow_jumpto = False


@exp.member(of_section="FQSection")
class FinalQuestionnaire2(al.Page):
    name = "finalquestionnaire_2"
    title = "Abschlussfragen"

    def on_exp_access(self):
        self += al.TextArea(
            toplab=content.suspicion_check,
            name="fq_suspicion_check",
            force_input=True,
        )


@exp.member(of_section="FQSection")
class FinalQuestionnaire5(al.Page):
    name = "demographics"
    title = "Demographische Angaben"

    def on_exp_access(self):
        choice_list = ["noch nicht ausgewählt", "weiblich", "männlich", "divers"]
        self += al.SingleChoiceList(
            leftlab="Bitte wähle das Geschlecht aus, dem du dich zugehörig fühlst.",
            *choice_list,
            name="gender",
            force_input=True,
        )
        self += al.NumberEntry(
            leftlab="Bitte gib dein Alter an.",
            suffix="Jahre",
            name="age",
            force_input=True,
        )
        self += al.TextEntry(
            leftlab="Falls du studierst, trage bitte deinen Studiengang ein.",
            force_input=True,
            name="course_of_studies",
        )


class SelectionPage(registration.SelectionPage):
    content = content.registration_selection_content

    pass


class RegistrationPage(registration.RegistrationPage):
    content = content.registration_page_content


@exp.member(of_section="main")
class EndSection(al.Section):
    allow_forward = True
    allow_backward = False
    allow_jumpfrom = False
    allow_jumpto = False


@exp.member(of_section="EndSection")
class MapeFeedbackPage(al.Page):
    title = "Feedback zu deiner Genauigkeit"
    name = "mape_feedback"

    def on_first_show(self):
        group = self.exp.plugins.group
        role = group.me.role
         # determine condition
        self.exp.condition = group.spec_name

        if role == "judge":
            estimation = []
            true_values = []
            for t in range(1, 21):
                estimation.append(
                    float(self.exp.values[f"trial_{t:02d}_final_estimate"])
                )
                true_values.append(
                    float(self.exp.values[f"true_value_{t}"])
                )
            estimation_list = list(estimation)
            true_values_list = list(true_values)

            ape_values = []
            for z in range(20):
                ape = (
                    abs(
                        (true_values_list[z] - estimation_list[z]) / true_values_list[z]
                    )
                    * 100
                )
                self += al.Value(ape, name=f"ape_{z}")
                # print(ape)
                ape_values.append(ape)
                # self += al.Text(
                #     text=f"Der APE in Aufgabe {z + 1} beträgt: {ape}", name=f"ape_trial{z + 1}"
                # )
            ape_list = list(ape_values)
            mape = round((sum(ape_list)) / len(ape_list))
            self += al.Value(mape, name=f"mean_ape")
            self += al.Alert(
                category="info",
                text="Der <b>Mean Absolute Percentage Error (MAPE)</b> ist ein statistisches Maß,"
                     " um die mittlere absolute prozentuale Abweichung zu bestimmen.<br>"
                     "Der MAPE gibt hier konkret an, wie stark die von dir geschätzten Werte von den "
                     "wahren (=tatsächlichen) Werten durchschnittlich abweichen. "
                     "Bei perfekter Übereinstimmung mit den wahren Werten beträgt der MAPE 0% (perfekte "
                     "Übereinstimmung), umso stärker die Schätzungen vom wahren Wert abweichen desto größer wird der "
                     "MAPE, es gibt dabei nach oben keine Grenze, der MAPE kann unendlich groß werden. <br>"
                     "Es gilt also: Je kleiner der MAPE, desto akkurater ist die durchschnittliche "
                     "Schätzung.",
            )
            self += al.Text(text=f"<b>Dein MAPE beträgt: {mape}%</b>", name=f"mape")

            threshold = 10
            count_below_threshold = len([x for x in ape_list if x < threshold])

            self += al.Text(text=f"Bei <b> {count_below_threshold} </b> der Aufgaben lag deine finale Schätzung"
                                 f" weniger als 10% vom wahren Wert entfernt.", name=f"ape_below_10perc")

            bonus_pay = round(count_below_threshold*0.15, 2)

            self += al.Text(text=f"Dir wird demnach ein Bonus von <b> {bonus_pay} €</b>  zusätzlich zu deiner festen "
                                 f"Vergütung ausgezahlt.", name=f"bonus_payout")

            self.exp.adata["payout"] = bonus_pay+7
        else:
            estimation = []
            true_values = []
            for x in range(1, 21):
                estimation.append(
                        float(self.exp.values[f"estimation_trial_{x:02}"])
                    )
                true_values.append(
                        float(self.exp.values[f"true_value_{x}"])
                    )

            estimation_list = list(estimation)
            true_values_list = list(true_values)
            # print(estimation_list)
            # print(true_values_list)

            ape_values = []
            for z in range(len(estimation_list)):
                ape = (
                    abs(
                        (true_values_list[z] - estimation_list[z]) / true_values_list[z]
                    )
                    * 100
                )
                self += al.Value(ape, name=f"ape_{z}")
                # print(ape)
                ape_values.append(ape)
                # self += al.Text(
                #     text=f"Der APE in Aufgabe {z + 1} beträgt: {ape}%", name=f"ape_trial{z + 1}"
                # )
            ape_list = list(ape_values)
            mape = round((sum(ape_list)) / len(ape_list))
            self += al.Value(mape, name=f"mean_ape")
            self += al.Alert(
                category="info",
                text="Der <b>Mean Absolute Percentage Error (MAPE)</b> ist ein statistisches Maß,"
                     " um die mittlere absolute prozentuale Abweichung zu bestimmen.<br>"
                     "Der MAPE gibt hier konkret an, wie stark die von dir geschätzten Werte von den "
                     "wahren (=tatsächlichen) Werten durchschnittlich abweichen. "
                     "Bei perfekter Übereinstimmung mit den wahren Werten beträgt der MAPE 0% (perfekte "
                     "Übereinstimmung), umso stärker die Schätzungen vom wahren Wert abweichen desto größer wird der "
                     "MAPE, es gibt dabei nach oben keine Grenze, der MAPE kann unendlich groß werden. <br>"
                     "Es gilt also: Je kleiner der MAPE, desto akkurater ist die durchschnittliche "
                     "Schätzung.",
            )
            self += al.Text(text=f"<b>Dein MAPE beträgt: {mape}%</b>", name=f"mape")
            self.exp.adata["payout"] = 7

@exp.member(of_section="EndSection")
class SelRegSection(al.Section):
    allow_forward = True
    allow_backward = True
    allow_jumpfrom = False
    allow_jumpto = False

    def validate_on_backward(self):
        pass

    def on_exp_access(self):
        self += SelectionPage()
        self += RegistrationPage()


@exp.as_final_page
class EndPage(al.Page):
    title = 'Erhebungsende'

    def on_exp_access(self):
        self += al.Text(content.debriefing_text)

        self += al.WebExitEnabler()
