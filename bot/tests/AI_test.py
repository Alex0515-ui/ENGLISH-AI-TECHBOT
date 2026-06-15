from AI.ai_practise import check_translation, build_check_prompt, generate_sentences
import pytest
from pytest_mock import mocker
from unittest.mock import Mock
import json


def test_build_prompt(mocker, db):
    """Verify correct prompt generation"""

    result = build_check_prompt("run", ["Я бегаю", "Он бежит"], "I run")

    assert "Target word: run" in result
    assert "1. Я бегаю" in result
    assert "User answer:" in result


@pytest.mark.asyncio
async def test_generating_sentences(mocker):
    """Test AI sentence generation"""

    mock_response = {
        "data": [
            {
                "word": "run",
                "ru_sentences": [
                    "Я бегаю каждое утро",
                    "Он бегает очень быстро"
                ]
            }
        ]
    }

    mock_completion = Mock()
    mock_completion.choices = [
        Mock(
            message=Mock(
                content=json.dumps(mock_response)
            )
        )
    ]

    mocker.patch("AI.ai_practise.client.chat.completions.create", return_value=mock_completion)

    result = await generate_sentences(["run", "hello"])

    assert result == mock_response["data"]


@pytest.mark.asyncio
async def test_check_translation(mocker):
    """Check if translation verification exists"""

    mock_ai = mocker.patch(
        "AI.ai_practise.client.chat.completions.create", 
        return_value=Mock(choices=[Mock(message=Mock(content="Correct."))])
    )

    await check_translation("run", ["Она бежит там"], "She runs there")

    mock_ai.assert_called_once()

    






