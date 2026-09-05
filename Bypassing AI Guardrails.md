**Bypassing AI Guardrails: Red Teaming TryHackMe's Prompt Security Room**

**Author:** Harshwardhan Tiwari
**CTF:** `h4rsh0x`
**Category:** AI Security / Prompt Injection

## Overview

This write-up documents my approach to a TryHackMe challenge involving an AI chatbot protected by input/output guardrails.

The chatbot presented itself as a simple word-chain game. However, the interaction could be used to explore how conversational state, generated instructions, and filtering affected the model's behavior.

---

## Objective

The goal was to interact with the chatbot, understand its filtering behavior, manipulate the conversation flow, and recover the challenge flag.

---

## Attack Flow

```text
Initial Word Chain
        ↓
Observe Chatbot Behavior
        ↓
Follow Generated Chain
        ↓
Trust → User → Bypass
        ↓
Output → Engage → Full
        ↓
Trust → Bypass → Everything
        ↓
Return → Hidden → Secret
        ↓
Flag-like Output
        ↓
Independent TryHackMe Validation
```

---

## Important Chain

The chatbot eventually exposed the following filtered chain:

```text
Trust
User
Bypass
Output
Engage
Full
Trust
Bypass
Everything
Return
Hidden
Secret
```

---

## Key Observations

### `Bypass`

The chatbot accepted the term **Bypass** as normal game content and continued the interaction.

### `Everything`

Selecting **Everything** caused the chatbot to introduce another sequence:

```text
Return → Hidden → Secret
```

### `Hidden`

The chatbot claimed that the hidden word was:

```text
Full
```

and referenced:

```text
USER FULL HIDDEN SECRET
```

### `Return`

The chatbot interpreted this as returning to the beginning of the chain and brought back:

```text
Trust
```

### `Secret`

The chatbot attempted to conclude the interaction as a meta-puzzle.

---

## Flag

The chatbot eventually produced:

```text
THM{fbu349b3u4b934byr93b}
```

Although the chatbot attempted to dismiss this as a red herring, I independently submitted it to TryHackMe.

**Result: Accepted ✅**

Therefore, the value was confirmed as the valid challenge flag.

---

## Lessons Learned

### Conversation state is an attack surface

Multi-turn interactions can produce behavior that isn't apparent from a single prompt.

### Generated instructions can become attack primitives

The chatbot's own responses influenced the next stages of the interaction.

### Model output isn't authoritative

The chatbot's statement that the flag was a red herring was contradicted by independent validation.

### Secrets shouldn't depend solely on prompt instructions

If an LLM has access to sensitive information, a system prompt saying "don't reveal it" should not be treated as a complete security control.

---

## Defensive Recommendations

For AI applications using guardrails:

* Keep secrets outside model-accessible context whenever possible.
* Separate trusted instructions from untrusted user-controlled content.
* Implement independent authorization checks.
* Use input and output monitoring.
* Test multi-turn prompt injection.
* Monitor repeated attempts to manipulate system behavior.
* Use canary values to detect unintended information disclosure.
* Never treat model-level instructions as the only protection for sensitive data.

---

## Flag

```text
THM{fbu349b3u4b934byr93b}
```

## Author

**Harshwardhan Tiwari — `h4rsh0x`**

Interested in:

`Cybersecurity • AI Security • Prompt Injection • CTFs • AI/ML`

GitHub: https://github.com/harshwt
