#!/usr/bin/env python3
"""Test Client File"""

import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """Test Github Org Client Class"""

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, test_org, mock_json):
        """Test Org Method"""
        client = GithubOrgClient(test_org)
        client.org()
        mock_json.assert_called_once_with(
            f"https://api.github.com/orgs/{test_org}"
        )

    def test_public_repos_url(self):
        """Test Public Repos Url Method"""
        with patch.object(
            GithubOrgClient,
            "org",
            new_callable=PropertyMock,
            return_value={'repos_url': 'holberton'}
        ) as mock_get:
            test_json = {"repos_url": 'holberton'}
            test_client = GithubOrgClient(test_json.get("repos_url"))
            test_return = test_client._public_repos_url
            mock_get.assert_called_once
            self.assertEqual(
                test_return,
                mock_get.return_value.get("repos_url")
            )
