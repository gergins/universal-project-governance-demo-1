/**
 * PORTING EXAMPLE ONLY — not a runnable test for the governance repository.
 * Copy into a product with @playwright/test installed and a configured webServer/baseURL.
 * Adapt role names, selectors and priority labels to the actual accessible product UI.
 * Never claim BROWSER_PASS before executing this against a real application.
 */
import { test, expect } from '@playwright/test';

test('task record is consistent across calendar and list after reload', async ({ page }) => {
  const title = 'Journey acceptance example';

  await page.goto('/');
  await page.getByRole('button', { name: 'New task' }).click();
  await page.getByRole('dialog').getByLabel('Title').fill(title);
  await page.getByRole('dialog').getByLabel('Due date').fill('2026-11-10');
  await page.getByRole('dialog').getByRole('button', { name: 'Save' }).click();

  await page.getByRole('navigation').getByRole('link', { name: 'Calendar' }).click();
  await page.getByRole('button', { name: title }).click();

  const details = page.getByRole('dialog', { name: 'Task details' });
  await expect(details.getByLabel('Title')).toHaveValue(title);
  await details.getByLabel('Priority').selectOption('high');
  await details.getByRole('button', { name: 'Save' }).click();

  await page.getByRole('navigation').getByRole('link', { name: 'My Tasks' }).click();
  await page.getByRole('button', { name: title }).click();
  await expect(page.getByRole('dialog', { name: 'Task details' }).getByLabel('Priority')).toHaveValue('high');

  await page.reload();
  await page.getByRole('button', { name: title }).click();
  await expect(page.getByRole('dialog', { name: 'Task details' }).getByLabel('Priority')).toHaveValue('high');
});

// Separate acceptance cases must cover keyboard activation, Escape/cancel,
// invalid input, storage/API failure, and responsive dialog positioning.
